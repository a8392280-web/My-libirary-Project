import requests 
import os
from datetime import datetime, timedelta
from config import OMDB_API_KEY, RAWG_API_KEY
from concurrent.futures import ThreadPoolExecutor


def get_game_info(game_name):
    api_key = RAWG_API_KEY
    url = "https://api.rawg.io/api/games"
    params = {
        "key": api_key,
        "search": game_name
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"❌ RAWG API error: {e}")
        return None

    if not data.get("results"):
        print("❌ No game found.")
        return None

    game = data["results"][0]
    game_info = {
        "Source": "Game",
        "Name": game.get("name") or "Unknown",
        "Released": game.get("released") or "Unknown",
        "Rating": game.get("rating") or "N/A",
        "Genres": [genre.get("name", "Unknown") for genre in game.get("genres", [])],
        "Image": game.get("background_image") or "N/A",
        "Platforms": [platform.get("platform", {}).get("name", "Unknown") for platform in game.get("platforms", [])]
    }

    # Loop until user approves
    
    print("\n🎮 Game Information:\n")
    for key, value in game_info.items():
        print(f"{key}: {value}")

    choice = input("\nDo you want to change any field? (yes/no): ").strip().lower()
    if choice == "yes":
        while True:

            for key in game_info.keys():
                if key == "Source":  # Can't change Source
                    continue

                new_value = input(f"Enter new value for '{key}' (leave empty to keep current): ").strip()
                if new_value:
                    if key in ("Genres", "Platforms"):
                        game_info[key] = [item.strip() for item in new_value.split(",")]
                    else:
                        game_info[key] = new_value

            print("\n✅ Updated Game Information:")
            for key, value in game_info.items():
                print(f"{key}: {value}")

            confirm = input("\nAre these changes good? (yes/no): ").strip().lower()
            if confirm == "yes":
                break
        

    return game_info
