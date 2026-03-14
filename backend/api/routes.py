from fastapi import APIRouter
import json

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