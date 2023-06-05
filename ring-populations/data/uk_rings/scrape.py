"""Get the population around a point for some UK cities
"""

import json
import csv
import time
import requests
from tqdm import tqdm

CITIES_CSV = "./ring-populations/data/worldcities/worldcities.csv"
OUTPUT_JSON = "./ring-populations/data/uk_rings/uk_rings.json"

SCRAPE_TOP_BY_POPULATION = 21
MAX_DISTANCE_KM = 20

RING_URL = "https://ringpopulationsapi.azurewebsites.net/api/globalringpopulations"


def get_rings(city):
    url = f"{RING_URL}?latitude={city['lat']}&longitude={city['lng']}&distance_km={MAX_DISTANCE_KM}"
    print(f"requesting\n{url}")
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    raise LookupError(
        f"Error getting rings for {city['city_ascii']}: {response.status_code}"
    )


def main():
    """Scrape data from population around a point for some UK cities"""

    # all cities
    all_cities = []
    with open(CITIES_CSV, "r", encoding="utf-8") as cities_file:
        cities_reader = csv.DictReader(cities_file)
        for city in cities_reader:
            all_cities.append(city)

    # uk cities
    uk_cities = [city for city in all_cities if city["country"] == "United Kingdom"]
    # by population
    uk_cities.sort(key=lambda city: int(city["population"]), reverse=True)
    # top N
    uk_cities = uk_cities[:SCRAPE_TOP_BY_POPULATION]

    # existing data
    with open(OUTPUT_JSON, "r", encoding="utf-8") as output_file:
        existing_data = json.load(output_file)

    # scrape
    for city in tqdm(uk_cities, total=len(uk_cities)):
        if (name := city["city_ascii"]) not in existing_data:
            print(f"Scraping {name}")
            data = get_rings(city)
            # transform
            distances = [ring["distance"] for ring in data]
            populations = [ring["people"] for ring in data]
            bus_stops = [ring["busStops"] for ring in data]
            tram_stops = [ring["tramStops"] for ring in data]
            rail_stops = [ring["railStops"] for ring in data]
            # write
            existing_data[name] = {
                "distances": distances,
                "populations": populations,
                "busStops": bus_stops,
                "tramStops": tram_stops,
                "railStops": rail_stops,
            }
            with open(OUTPUT_JSON, "w", encoding="utf-8") as output_file:
                json.dump(existing_data, output_file, separators=(",", ":"))
            # wait
            time.sleep(1)

    print("Done")


if __name__ == "__main__":
    main()
