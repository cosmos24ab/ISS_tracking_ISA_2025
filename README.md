# 🛰️ ISS Tracker Dashboard

This project provides a real-time dashboard for tracking the International Space Station (ISS) using Python. It features both a Jupyter Notebook for exploratory learning and a live web application built with Streamlit.

The Jupyter Notebook (`iss_tracker_ISA2025.ipynb`) guides users through key concepts such as geolocation, satellite orbital mechanics using TLE (Two-Line Element) data, and satellite propagation using the Skyfield library. It is an excellent starting point for understanding how satellite tracking works under the hood.

The Streamlit application (`iss_dashboard.py`) offers a clean and interactive interface for live ISS tracking. Users can select a city, and the app displays the current position of the ISS on a dynamic map, updating in near real-time. The application uses data from the Open Notify API to fetch the latest ISS coordinates and renders them using Folium maps embedded in the Streamlit frontend.

To get started, make sure to install the required Python dependencies listed in `requirements.txt`. You can then launch the notebook in Jupyter for step-by-step exploration, or run the Streamlit app to view the live dashboard.

This project is built using open-source tools and datasets. Orbital data is sourced from [CelesTrak](https://celestrak.org/), while the Skyfield library (developed by Brandon Rhodes) handles the satellite position calculations. The web interface is powered by [Streamlit](https://streamlit.io/), which makes building data apps in Python both fast and intuitive.

---

**Credits**  
- [CelesTrak](https://celestrak.org/) – for providing up-to-date TLE data  
- [Skyfield](https://rhodesmill.org/skyfield/) – for accurate satellite propagation  
- [Streamlit](https://streamlit.io/) – for building the interactive dashboard interface

---


