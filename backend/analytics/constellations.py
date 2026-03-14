import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_FILE = BASE_DIR / "data" / "processed_satellites.json"

def get_starlink_satellites():
    with open(DATA_FILE) as f:
        satellites = json.load(f)
    starlink_satellites = []
    for sat in satellites:
        if "STARLINK" in sat["name"].upper():
            starlink_satellites.append({
                "name": sat["name"],
                "latitude": sat["latitude"],
                "longitude": sat["longitude"],
                "altitude_km": sat["altitude_km"]
            })
    return {
        "constellation": "Starlink",
        "count": len(starlink_satellites),
        "satellites": starlink_satellites
    }