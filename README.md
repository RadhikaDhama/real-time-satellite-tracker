# 🌍 Real-Time Satellite Tracker

A full-stack web application that visualizes satellites orbiting Earth in real time.

The system collects satellite orbital data from public datasets, processes the data using orbital mechanics libraries, and exposes APIs that power an interactive visualization platform.

The application allows users to explore satellite constellations, analyze orbital distributions, and understand how satellites move around Earth.

---

#  Problem Statement

Build a web application that visualizes satellites orbiting Earth in real time.

The application should:

• Display real-time satellite positions
• Show orbital paths around Earth
• Allow filtering satellites by category
• Provide insights into satellite distribution

The system should also help users understand how satellite constellations operate.

---

# 🛰 Project Overview

The system consists of two main components.

## Backend (Radhika Dhama – Data & Backend)

Responsible for:

• Collecting satellite data from TLE datasets
• Converting orbital elements into geographic coordinates
• Calculating satellite velocity and altitude
• Building backend APIs for frontend visualization
• Generating analytics and statistics

---

## Frontend (Ankush Agrawal – Web Application & Visualization)

Responsible for:

• Interactive Earth map or globe visualization
• Displaying satellites moving in real time
• Orbit path rendering
• Satellite search and filtering
• Analytics dashboards

---

# 📡 Data Sources

Satellite data is obtained from publicly available datasets.

### Satellite Orbit Data (TLE)

https://celestrak.org/NORAD/elements

### Starlink Satellite Data

https://celestrak.org/NORAD/elements/starlink.txt

### Satellite Position APIs

https://api.wheretheiss.at
https://www.n2yo.com/api

---

#  System Architecture

```
Celestrak TLE Data
        ↓
Data Ingestion
(fetch_tle.py)
        ↓
Satellite Propagation
(Skyfield Library)
        ↓
Processed Satellite Dataset
(processed_satellites.json)
        ↓
FastAPI Backend
        ↓
Analytics + Orbit Prediction APIs
        ↓
Frontend Visualization
```

---

#  Backend Features

## Satellite Data Processing

The backend processes satellite orbital data and extracts useful attributes.

Each satellite record contains:

```
name
latitude
longitude
altitude_km
velocity_km_s
category
operator
```

### Processing Steps

1. Fetch TLE datasets from Celestrak
2. Parse orbital elements
3. Propagate orbit using **Skyfield**
4. Convert orbital coordinates to geographic coordinates
5. Calculate velocity of satellites
6. Detect satellite operator
7. Classify satellite category

---

#  Real-Time Satellite Updates

The backend simulates real-time tracking by periodically updating satellite positions.

Technology used:

```
APScheduler
```

Satellite positions refresh every **30 seconds**.

---

# 🌐 API Endpoints

## Satellite Data

### Get All Satellites

```
GET /satellites
```

Returns real-time satellite dataset.

---

### Search Satellite

```
GET /satellite?name=ISS
```

Returns a specific satellite.

---

## Orbit Prediction

### Predict Orbit Path

```
GET /orbit/{satellite_name}
```

Returns predicted orbit path for the next **3 hours**.

Example output:

```
{
  "satellite": "ISS",
  "orbit_path": [
    {"latitude": 10.5, "longitude": 80.2, "altitude_km": 420}
  ]
}
```

---

## Satellite Constellations

### Starlink Constellation

```
GET /constellations/starlink
```

Returns all Starlink satellites.

---

## Satellite Analytics

### Satellites by Orbit Type

```
GET /statistics/orbits
```

Returns:

```
LEO
MEO
GEO
```

---

### Satellites by Operator

```
GET /statistics/operators
```

Example:

```
SpaceX
NASA
NOAA
Other
```

---

### Satellites by Altitude Range

```
GET /statistics/altitudes
```

Returns satellite distribution by altitude.

---

### Satellites by Category

```
GET /statistics/categories
```

Returns satellites grouped by:

```
communication
navigation
weather
scientific
```

---

#  Data Insights Dashboard

The backend APIs support visual dashboards such as:

• satellites by orbit type
• satellites by altitude
• satellites by operator
• satellites by category

Visualization libraries that may be used:

```
Chart.js
D3.js
ECharts
```

---

#  Bonus Features Implemented

## Starlink Constellation Visualization

The system detects and highlights **Starlink satellites**.

---

## Orbit Path Prediction

Users can click a satellite and view its **future orbit path**.

---

## Real-Time Simulation

Satellite positions update automatically using a scheduler.

---

#  Screenshots

### Satellite Map Visualization

![Satellite Map](screenshots/map_view.png)

---

### Orbit Prediction Visualization

![Orbit Prediction](screenshots/orbit_prediction.png)

---

### Analytics Dashboard

![Analytics Dashboard](screenshots/analytics_dashboard.png)

---

# Setup Instructions

## Clone Repository

```
git clone https://github.com/RadhikaDhama/real-time-satellite-tracker.git
```

---

## Navigate to Project

```
cd satellite-tracker
```

---

## Create Virtual Environment

```
python -m venv venv
```

---

## Activate Environment

Windows

```
venv\Scripts\activate
```

---

## Install Dependencies

```
pip install -r requirements.txt
```

---

## Generate Satellite Dataset

```
python backend/processing/propagate_satellite.py
```

---

## Run Backend Server

```
uvicorn backend.main:app --reload
```

---

## Access API Documentation

```
http://127.0.0.1:8000/docs
```

---

#  Project Structure

```
satellite-tracker
│
├── backend
│   ├── ingestion
│   ├── processing
│   ├── analytics
│   ├── services
│   ├── api
│   └── main.py
│
├── data
│
├── screenshots
│
├── README.md
└── requirements.txt
```

---

#  Technologies Used

## Backend

```
Python
FastAPI
Skyfield
APScheduler
```

---

## Frontend (planned)

```
Leaflet
CesiumJS
Three.js
Chart.js
```

---

# GitHub Collaboration

The project uses GitHub for collaboration.

Branches used:

```
main
backend
frontend
```

Both candidates work on separate branches and merge changes using pull requests.

---
