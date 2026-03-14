import json
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_FILE = BASE_DIR / "data" / "processed_satellites.json"

def compute_analytics():
    with open(DATA_FILE) as f:
        satellites = json.load(f)
    orbit_distribution = {
        "LEO": 0,
        "MEO": 0,
        "GEO": 0
    }
    operators = []
    for sat in satellites:
        altitude = sat["altitude_km"]
        if altitude < 2000:
            orbit_distribution["LEO"] += 1
        elif altitude < 35000:
            orbit_distribution["MEO"] += 1
        else:
            orbit_distribution["GEO"] += 1
        name = sat["name"].upper()
        if "STARLINK" in name:
            operators.append("SpaceX")
        elif "ISS" in name:
            operators.append("NASA")
        else:
            operators.append("Other")
    operator_distribution = Counter(operators)
    return {
        "satellite_count": len(satellites),
        "orbit_distribution": orbit_distribution,
        "operator_distribution": dict(operator_distribution)
    }