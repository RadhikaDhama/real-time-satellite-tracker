import requests

url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle"

response = requests.get(url)

with open("data/tle_cache.txt", "w") as f:
    f.write(response.text)

print("TLE data downloaded successfully")