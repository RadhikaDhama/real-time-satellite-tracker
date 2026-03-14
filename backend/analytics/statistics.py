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

        alt = sat["altitude_km"]

        if alt < 2000:
            orbit_counts["LEO"] += 1
        elif alt < 35000:
            orbit_counts["MEO"] += 1
        else:
            orbit_counts["GEO"] += 1

    return orbit_counts


def operator_statistics():

    with open("data/processed_satellites.json") as f:
        satellites = json.load(f)

    operators = [sat["operator"] for sat in satellites]

    return dict(Counter(operators))


def altitude_statistics():

    with open("data/processed_satellites.json") as f:
        satellites = json.load(f)

    ranges = {
        "0-500 km": 0,
        "500-1000 km": 0,
        "1000-5000 km": 0,
        "5000+ km": 0
    }

    for sat in satellites:

        alt = sat["altitude_km"]

        if alt < 500:
            ranges["0-500 km"] += 1
        elif alt < 1000:
            ranges["500-1000 km"] += 1
        elif alt < 5000:
            ranges["1000-5000 km"] += 1
        else:
            ranges["5000+ km"] += 1

    return ranges


def category_statistics():

    with open("data/processed_satellites.json") as f:
        satellites = json.load(f)

    categories = [sat["category"] for sat in satellites]

    return dict(Counter(categories))