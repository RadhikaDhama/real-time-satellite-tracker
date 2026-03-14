import requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TLE_FILE = BASE_DIR / "data" / "tle_cache.txt"

url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"
response = requests.get(url)
with open(TLE_FILE, "w") as f:
    f.write(response.text)
print("TLE data downloaded successfully")