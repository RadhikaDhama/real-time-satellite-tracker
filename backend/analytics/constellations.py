import json


def get_starlink_satellites():

    with open("data/processed_satellites.json") as f:
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