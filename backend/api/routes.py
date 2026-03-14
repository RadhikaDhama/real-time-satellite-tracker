from fastapi import APIRouter
import json
from analytics.satellite_metrics import compute_analytics
from analytics.constellations import get_starlink_satellites
from processing.orbit_prediction import predict_orbit
from analytics.statistics import orbit_statistics
from analytics.statistics import operator_statistics
from analytics.statistics import altitude_statistics

router = APIRouter()


@router.get("/satellites")
def get_satellites():

    with open("data/processed_satellites.json") as f:
        satellites = json.load(f)

    return satellites


@router.get("/satellite")
def search_satellite(name: str):

    with open("data/processed_satellites.json") as f:
        satellites = json.load(f)

    for sat in satellites:

        if name.lower() in sat["name"].lower():
            return sat

    return {"message": "Satellite not found"}
@router.get("/analytics")
def get_analytics():

    analytics = compute_analytics()

    return analytics

@router.get("/constellations/starlink")
def starlink_constellation():

    return get_starlink_satellites()

@router.get("/orbit/{satellite_name}")
def get_orbit(satellite_name: str):

    return predict_orbit(satellite_name)

@router.get("/statistics/orbits")
def get_orbit_statistics():

    return orbit_statistics()

@router.get("/statistics/operators")
def get_operator_statistics():

    return operator_statistics()

@router.get("/statistics/altitudes")
def get_altitude_statistics():

    return altitude_statistics()