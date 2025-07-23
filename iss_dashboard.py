import streamlit as st
from datetime import datetime, timedelta, timezone
from skyfield.api import load, EarthSatellite, Topos
import matplotlib.pyplot as plt
import requests

# Load Skyfield timescale
ts = load.timescale()

# Predefined city coordinates (India)
cities = {
    "Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Bengaluru": (12.9716, 77.5946),
    "Kolkata": (22.5726, 88.3639),
    "Hyderabad": (17.3850, 78.4867)
}

# Fetch the latest TLE data for the ISS
@st.cache_data(ttl=3600)
def fetch_iss_tle():
    url = "https://celestrak.org/NORAD/elements/stations.txt"
    response = requests.get(url)
    lines = response.text.strip().split('\n')
    for i in range(len(lines)):
        if "ISS" in lines[i]:
            return lines[i], lines[i + 1], lines[i + 2]
    raise Exception("ISS TLE not found in data.")

# Plot ground track of the ISS
def plot_ground_track(satellite, duration_minutes=90):
    start_time = datetime.now(timezone.utc)
    times = ts.from_datetimes([start_time + timedelta(minutes=i) for i in range(duration_minutes)])

    lats, lons = [], []
    for t in times:
        subpoint = satellite.at(t).subpoint()
        lats.append(subpoint.latitude.degrees)
        lons.append(subpoint.longitude.degrees)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(lons, lats, label='ISS Path')
    ax.scatter(lons[0], lats[0], color='red', label='Current Position')
    ax.set_title(f"ISS Ground Track (Next {duration_minutes} Minutes)")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.grid(True)
    ax.legend()
    return fig

# ---- Streamlit App ----
st.set_page_config(page_title="ISS Tracker", layout="centered")
st.title("🛰 Real-Time ISS Tracker")
st.markdown("Track the International Space Station in real-time and predict its next pass over major Indian cities.")

# Fetch satellite object
name, line1, line2 = fetch_iss_tle()
satellite = EarthSatellite(line1, line2, name, ts)

# User inputs
city = st.selectbox("📍 Choose a city:", list(cities.keys()))
duration = st.slider("⏱ Ground track duration (minutes):", 30, 180, 90, step=10)

# Location from city
lat, lon = cities[city]
location = Topos(latitude_degrees=lat, longitude_degrees=lon)

# Predict next ISS pass
st.subheader(f"🌐 Next ISS Pass Over {city}")
t0 = ts.from_datetime(datetime.now(timezone.utc))
t1 = ts.from_datetime(datetime.now(timezone.utc) + timedelta(days=1))

try:
    times, events = satellite.find_events(location, t0, t1, altitude_degrees=30.0)
    event_labels = ['Rise 🌅', 'Culminate 🌕', 'Set 🌇']
    for t, e in zip(times, events):
        st.write(f"{event_labels[e]}: {t.utc_datetime():%Y-%m-%d %H:%M:%S UTC}")
except Exception:
    st.warning("⚠️ Could not calculate pass times. Try again later or select a different city.")

# Plot the ISS ground track
st.subheader("🗺️ ISS Ground Track")
fig = plot_ground_track(satellite, duration)
st.pyplot(fig)
