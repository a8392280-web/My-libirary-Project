import requests 
import os
from datetime import datetime, timedelta
from config import OMDB_API_KEY, RAWG_API_KEY
from concurrent.futures import ThreadPoolExecutor


def get_manga_info(manga_name):
    url = 'https://kitsu.io/api/edge/manga'
    params = {'filter[text]': manga_name}

    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ Kitsu API error: {e}")
        return None

    data = resp.json()
    manga_list = data.get('data', [])
    if not manga_list:
        print("❌ Manga not found.")
        return None

    manga = manga_list[0]
    manga_id = manga.get('id')
    attributes = manga.get('attributes', {})

    # Fetch genres
    try:
        genre_url = f"https://kitsu.io/api/edge/manga/{manga_id}/genres"
        genre_resp = requests.get(genre_url, timeout=10)
        genre_resp.raise_for_status()
        genres_data = genre_resp.json().get('data', [])
        genres = [g.get('attributes', {}).get('name', 'Unknown') for g in genres_data]
    except requests.RequestException:
        genres = ["Unknown"]

    manga_info = {
        "Source": "Manga",
        "Name": attributes.get('titles', {}).get('en_jp', 'Unknown'),
        "Released": attributes.get('startDate') or "Unknown",
        "Rating": "N/A",
        "Genres": genres,
        "Image": attributes.get('posterImage', {}).get('small', 'N/A'),
        "Plot": attributes.get('synopsis') or "N/A",
        "Chapters": attributes.get('chapterCount') or "Unknown"
    }


    print("\n📚 Manga Information:")
    for key, value in manga_info.items():
        print(f"{key}: {value}")

    choice = input("\nDo you want to change any field? (yes/no): ").strip().lower()
    if choice == "yes":
        while True:
            for key in manga_info.keys():
                if key == "Source":  # Cannot change source
                    continue

                new_value = input(f"Enter new value for '{key}' (leave empty to keep current): ").strip()
                if new_value:
                    if key == "Genres":
                        manga_info[key] = [genre.strip() for genre in new_value.split(",")]
                    else:
                        manga_info[key] = new_value

            print("\n✅ Updated Manga Information:")
            for key, value in manga_info.items():
                print(f"{key}: {value}")

            confirm = input("\nAre these changes good? (yes/no): ").strip().lower()
            if confirm == "yes":
                break

    return manga_info
