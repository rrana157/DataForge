import geonamescache
import pycountry
import requests
import json
import pycountry_convert


url = "http://download.geonames.org/export/dump/admin1CodesASCII.txt"
response = requests.get(url)
lines = response.text.strip().split("\n")

admin1_dict = {}
for line in lines:
    parts = line.split("\t")
    if len(parts) >= 3:
        code = parts[0]  # e.g., IN.16
        state_name = parts[2]
        admin1_dict[code] = state_name

gc = geonamescache.GeonamesCache()
cities = gc.get_cities()
countries = gc.get_countries()
alpha2_to_alpha3 = {c.alpha_2: c.alpha_3 for c in pycountry.countries}

continent_map = {
    'AF': 'Africa',
    'AS': 'Asia',
    'EU': 'Europe',
    'NA': 'North America',
    'OC': 'Oceania',
    'SA': 'South America',
    'AN': 'Antarctica'
}

data = []

for city_id, city in cities.items():
    country_code = city['countrycode']
    admin1_code = city.get('admin1code')

    if not admin1_code:
        continue

    admin1_key = f"{country_code}.{admin1_code}"
    state_name = admin1_dict.get(admin1_key)

    if not state_name:
        state_name = ""

    country_info = countries.get(country_code, {})
    country_name = country_info.get('name', '')
    alpha3 = alpha2_to_alpha3.get(country_code, '')

    city_name = city['name']
    lat = float(city['latitude'])
    lon = float(city['longitude'])

    try:
        continent_code = pycountry_convert.country_alpha2_to_continent_code(country_code)
        region = continent_map.get(continent_code, "Other")
    except Exception:
        region = "Other"

    data.append({
        "Region" : region,
        "Country": country_name,
        "State": state_name,
        "City": city_name,
        "Latitude": lat,
        "Longitude": lon,
        "Alpha-2": country_code,
        "Alpha-3": alpha3
    })

with open("../data_libraries/world_cities.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
