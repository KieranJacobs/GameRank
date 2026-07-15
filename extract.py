import os
from dotenv import load_dotenv
import requests
import json

# 1. connect to RAWG API endpoint (https://api.rawg.io/api/games)
load_dotenv()

my_credential = os.getenv("RAWG_API_KEY")


def fetch_top_games():
    """Fetches top 50 games from RAWG API ordered by rating."""
    url = "https://api.rawg.io/api/games"

    # 2. request top 50 games ordered by rating
    params = {
        "key": my_credential,
        "page_size": 50,
        "ordering": "-rating",  # Highest rated first
        "dates": "2020-01-01,2026-12-31",  # games released in 2020's to now
    }

    response = requests.get(url, params=params)

    # 3. check for a successful connection
    if response.status_code == 200:
        data = response.json()

        # 4. save the output list to json
        with open("raw_games.json", "w", encoding="utf-8") as file:
            json.dump(data["results"], file, indent=4)

        print("50 games saved to raw_games.json sucessfully.")
    else:
        print(f"failed to fetch data. Status Code: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    fetch_top_games()
