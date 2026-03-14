# Real-Time Satellite Tracker

A web-based system that visualizes satellites orbiting Earth in real time.  
The project retrieves satellite orbital data from public datasets, processes it using orbital mechanics libraries, and exposes APIs for real-time visualization on an interactive map or globe.

This project is developed as part of an internship assignment to demonstrate backend data processing, API development, and satellite analytics.

## Problem Statement

Build a web application that visualizes satellites orbiting Earth in real time.

The application should:

- Display satellite positions around Earth
- Show orbital paths
- Allow filtering satellites by category
- Provide insights into satellite distribution

Users should be able to explore different satellite constellations such as communication satellites, navigation satellites, and scientific satellites.

## Project Overview

The system consists of two main components:

### Backend (Student 1)

Responsible for:

- Collecting satellite orbital data
- Processing Two-Line Element (TLE) datasets
- Converting orbital elements into geographic coordinates
- Providing APIs for the frontend
- Generating satellite analytics and statistics

### Frontend (Student 2)

Responsible for:

- Interactive globe or map visualization
- Satellite filtering and search
- Displaying satellite information panels
- Rendering orbit paths
- Building analytics dashboards

## Data Sources

Satellite data is obtained from publicly available datasets.

### Satellite TLE Data
https://celestrak.org/NORAD/elements

### Starlink Satellite Data
https://celestrak.org/NORAD/elements/starlink.txt

### Satellite Position APIs
https://api.wheretheiss.at
https://www.n2yo.com/api

## System Architecture

Satellite data flows through several stages.

TLE Data Source  
↓  
Data Ingestion  
↓  
Satellite Propagation using Skyfield  
↓  
Processed Satellite Dataset  
↓  
FastAPI Backend APIs  
↓  
Frontend Visualization

## Backend Features

The backend system provides the following functionality:

### Satellite Data Processing
- TLE data ingestion
- Satellite orbit propagation
- Conversion of orbital elements into geographic coordinates

### Satellite Tracking APIs
- Retrieve real-time satellite positions
- Search satellites by name
- Predict orbit paths

### Satellite Analytics
- Satellites by orbit type (LEO, MEO, GEO)
- Satellites by operator
- Satellite altitude distribution

### Constellation Detection
- Detection of Starlink satellites

## API Endpoints

### Satellite Data

GET /satellites  
Returns all satellite positions.

GET /satellite?name=ISS  
Search for a satellite by name.

### Orbit Prediction

GET /orbit/{satellite_name}  
Returns predicted orbit path for the satellite.

### Constellations

GET /constellations/starlink  
Returns Starlink satellites.

### Analytics

GET /analytics  
Returns overall satellite analytics.

### Statistics

GET /statistics/orbits  
Returns satellite distribution by orbit type.

GET /statistics/operators  
Returns satellites grouped by operator.

GET /statistics/altitudes  
Returns satellites grouped by altitude ranges.

## Setup Instructions

### Clone the Repository

git clone https://github.com/RadhikaDhama/real-time-satellite-tracker.git

### Navigate to Project

cd satellite-tracker

### Create Virtual Environment

python -m venv venv

### Activate Environment

Windows:

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Run Backend Server

uvicorn backend.main:app --reload

### Access API

http://127.0.0.1:8000/docs