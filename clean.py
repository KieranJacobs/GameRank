# clean.py

# 1. File ingestion - Open and Read local raw_games.json file
# 2. Record Iteration - loop through the list of game dictionaries.
# 3. Conditional Filtering - Check if each game meets your criteria. Filter out any game where [released]
#    date string is missing, or the [metacritic] score is [None] or below [75]
# 4. Output Export - Save new filtered list of clean game dictionaries to clean_games.json

import json

# open file in read-mode
with open("raw_games.json", "r", encoding="utf-8") as file:
    # convert raw json string back into Python data structure
    loaded_games = json.load(file)

    # Filter to fit criteria: released = "release_date_here", metacritic != null or metacritic < 75
clean_games = []
for game in loaded_games:
    released = game.get("released")
    metacritic = game.get("metacritic")

    if released and metacritic is not None and metacritic >= 75:
        clean_games.append(
            {
                "name": game.get("name"),
                "released": released,
                "metacritic": metacritic,
            }
        )

with open("clean_games.json", "w", encoding="utf-8") as clean:
    json.dump(clean_games, clean, indent=4)
