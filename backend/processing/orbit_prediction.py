from skyfield.api import EarthSatellite, load


def predict_orbit(satellite_name):

    with open("data/tle_cache.txt") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    ts = load.timescale()

    for i in range(0, len(lines), 3):

        name = lines[i]

        if satellite_name.lower() in name.lower():

            line1 = lines[i + 1]
            line2 = lines[i + 2]

            satellite = EarthSatellite(line1, line2, name, ts)

            orbit_points = []

            for minute in range(0, 180, 5):

                t = ts.now() + minute / 1440

                geocentric = satellite.at(t)
                subpoint = geocentric.subpoint()

                orbit_points.append({
                    "latitude": subpoint.latitude.degrees,
                    "longitude": subpoint.longitude.degrees,
                    "altitude_km": subpoint.elevation.km
                })

            return {
                "satellite": name,
                "orbit_path": orbit_points
            }

    return {"message": "Satellite not found"}