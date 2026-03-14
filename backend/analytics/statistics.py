import json
from collections import Counter


def orbit_statistics():

    with open("data/processed_satellites.json") as f:
        satellites = json.load(f)

    orbit_counts = {
        "LEO": 0,
        "MEO": 0,
        "GEO": 0
    }

    for sat in satellites:

        altitude = sat["altitude_km"]

        if altitude < 2000:
            orbit_counts["LEO"] += 1
        elif altitude < 35000:
            orbit_counts["MEO"] += 1
        else:
            orbit_counts["GEO"] += 1

    return orbit_counts


def operator_statistics():

    with open("data/processed_satellites.json") as f:
        satellites = json.load(f)

    operators = []

    for sat in satellites:

        name = sat["name"].upper()

        if "STARLINK" in name:
            operators.append("SpaceX")
        elif "ISS" in name:
            operators.append("NASA")
        else:
            operators.append("Other")

    return dict(Counter(operators))


def altitude_statistics():

    with open("data/processed_satellites.json") as f:
        satellites = json.load(f)

    altitude_ranges = {
        "0-500 km": 0,
        "500-1000 km": 0,
        "1000-5000 km": 0,
        "5000+ km": 0
    }

    for sat in satellites:

        altitude = sat["altitude_km"]

        if altitude < 500:
            altitude_ranges["0-500 km"] += 1
        elif altitude < 1000:
            altitude_ranges["500-1000 km"] += 1
        elif altitude < 5000:
            altitude_ranges["1000-5000 km"] += 1
        else:
            altitude_ranges["5000+ km"] += 1

    return altitude_ranges