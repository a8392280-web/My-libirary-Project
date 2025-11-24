import requests 
from concurrent.futures import ThreadPoolExecutor
from config import OMDB_API_KEY

BASE_URL = "http://www.omdbapi.com/"
session = requests.Session()


def omdb_request(params):
    params["apikey"] = OMDB_API_KEY
    try:
        r = session.get(BASE_URL, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        return data if data.get("Response") == "True" else None
    except:
        return None


def get_series_info(title_name):
    """
    Return dict containing SERIES info including seasons + episodes.
    Returns: dict | "no" | "not series"
    """
    base = omdb_request({"t": title_name})
    if not base:
        return "no"

    if base.get("Type") != "series":
        return "not series"

    # Handle missing totalSeasons
    total_seasons = int(base.get("totalSeasons", 0)) if base.get("totalSeasons") else 1

    def fetch_season(sn):
        season_data = omdb_request({"t": title_name, "Season": sn})
        if not season_data:
            return None

        episodes = [
            {
                "Episode": ep.get("Episode"),
                "Title": ep.get("Title"),
                "Released": ep.get("Released"),
                "imdbRating": ep.get("imdbRating"),
                "imdbID": ep.get("imdbID"),
            }
            for ep in season_data.get("Episodes", [])
        ]

        return {"Season": sn, "Episodes": episodes}

    # Fetch seasons concurrently
    with ThreadPoolExecutor() as executor:
        seasons = list(filter(None, executor.map(fetch_season, range(1, total_seasons + 1))))

    # If OMDB didn't return individual seasons → fallback to Season 1
    if not seasons and base.get("Episodes"):
        episodes = [
            {
                "Episode": ep.get("Episode"),
                "Title": ep.get("Title"),
                "Released": ep.get("Released"),
                "imdbRating": ep.get("imdbRating"),
                "imdbID": ep.get("imdbID"),
            }
            for ep in base.get("Episodes", [])
        ]
        seasons = [{"Season": 1, "Episodes": episodes}]

    return {
        "Source": "Series",
        "Name": base.get("Title", "Unknown"),
        "Released": base.get("Year"),
        "Rating": base.get("imdbRating"),
        "imdb_id": base.get("imdbID"),
        "Genres": [g.strip() for g in base.get("Genre", "").split(",")] if base.get("Genre") else [],
        "Image": base.get("Poster"),
        "Plot": base.get("Plot"),
        "Seasons": seasons
    }