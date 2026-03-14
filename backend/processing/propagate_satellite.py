import json
from pathlib import Path
from skyfield.api import EarthSatellite, load

TLE_FILE = Path("data/tle_cache.txt")
OUTPUT_FILE = Path("data/processed_satellites.json")


def parse_tle():

    satellites = []

    with open(TLE_FILE, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    for i in range(0, len(lines), 3):

        try:
            name = lines[i]
            line1 = lines[i+1]
            line2 = lines[i+2]

            satellites.append({
                "name": name,
                "line1": line1,
                "line2": line2
            })

        except:
            continue

    return satellites


def compute_positions():

    ts = load.timescale()
    t = ts.now()

    satellites = parse_tle()

    results = []

    for sat in satellites[:2000]:

        satellite = EarthSatellite(
            sat["line1"],
            sat["line2"],
            sat["name"],
            ts
        )

        geocentric = satellite.at(t)
        subpoint = geocentric.subpoint()

        results.append({
            "name": sat["name"],
            "latitude": subpoint.latitude.degrees,
            "longitude": subpoint.longitude.degrees,
            "altitude_km": subpoint.elevation.km
        })

    return results


def save_satellites():

    satellites = compute_positions()

    with open(OUTPUT_FILE, "w") as f:
        json.dump(satellites, f, indent=4)

    print("Satellite positions saved:", len(satellites))


if __name__ == "__main__":
    save_satellites()
