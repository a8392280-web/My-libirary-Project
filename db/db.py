import json
import os
from typing import Callable, Dict, Any
from datetime import datetime, timedelta
from api.info_from_APIs import update_imdb_info_if_old
# --------------------------- Setup --------------------------- #

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "DB")
MOVIES_PATH = os.path.join(DATA_DIR, "movies.json")

# Optional UI callback
on_movies_saved: Callable[[], None] | None = None # learn about it


# --------------------------- Initialization --------------------------- #

def init_movies_file() -> None:
    """Ensure the DB folder and movies.json file exist."""
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(MOVIES_PATH):
        save_movies({"watching": [], "watched": []})  # Default structure


# --------------------------- Load & Save --------------------------- #

def load_movies() -> Dict[str, Any]: # learn about it
    """Load all movie data safely."""
    init_movies_file()
    try:
        with open(MOVIES_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Reset corrupt file
        print("⚠️ movies.json was corrupted. Resetting...")
        save_movies({"watching": [], "watched": []})
        return {"watching": [], "watched": []}


def save_movies(movies: Dict[str, Any]) -> None:
    """Save movie data to JSON file and trigger callback if present."""
    init_movies_file()
    with open(MOVIES_PATH, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=4, ensure_ascii=False)

    if on_movies_saved:
        on_movies_saved()


# --------------------------- Utility --------------------------- #

def new_id(section: str, start_id: int = 1) -> int:
    """Generate a unique ID for a given section."""
    data = load_movies()
    existing_ids = {m.get("id") for m in data.get(section, []) if m.get("id") is not None}
    while start_id in existing_ids:
        start_id += 1
    return start_id


def upadate_imdb_rating(movie,section , id):
        "update the imdb rating"
        updated_movie = update_imdb_info_if_old(movie)
        if updated_movie:
            print("OLD:", movie.get("Rating"))
            print("NEW:", updated_movie["Rating"])
            data = load_movies()
            for m in data[section]:
                if m["id"] == id:
                    m["Rating"] = updated_movie["Rating"]
                    m["last_updated"] = updated_movie["last_updated"]
                    save_movies(data)
                    print("✅ IMDb rating updated and saved!")
                    movie = updated_movie
                    return movie
            else:
                return None
        else:
            return None

# --------------------------- Core Operations --------------------------- #

def move_movie(from_section: str, to_section: str, movie_id: int) -> bool:
    """Move a movie from one section to another safely."""
    data = load_movies()
    from_list = data.get(from_section, [])
    to_list = data.get(to_section, [])

    # Find movie
    movie = next((m for m in from_list if m.get("id") == movie_id), None)
    if not movie:
        print(f"⚠️ Movie with id={movie_id} not found in '{from_section}'.")
        return False

    # Assign new unique ID in destination
    movie["id"] = new_id(to_section)
    to_list.append(movie)
    from_list.remove(movie)

    # Save
    data[from_section] = from_list
    data[to_section] = to_list
    save_movies(data)
    print(f"✅ Moved movie id={movie_id} from '{from_section}' → '{to_section}'.")
    return True


def delete_movie(section: str, movie_id: int) -> bool:
    """Delete a movie by ID from a given section."""
    data = load_movies()
    movies = data.get(section, [])
    new_list = [m for m in movies if m.get("id") != movie_id] # new list without the element we want to delete.

    if len(new_list) == len(movies):
        print(f"⚠️ Movie with id={movie_id} not found in '{section}'.")
        return False

    data[section] = new_list
    save_movies(data)
    print(f"🗑️ Deleted movie id={movie_id} from '{section}'.")
    return True


def add_movie(section: str, name: str, runtime: str, released: str,
              genres: list[str], image_url: str,
              rating: str = "", plot: str = "" , user_rating: str = "" , imdb_id: str = "") -> bool:
    """
    Add a new movie to the given section.

    Args:
        section: Section name (e.g., "watching", "watched", "want_to_watch").
        name: Movie title.
        runtime: Duration (e.g., "148 min").
        released: Release year or date.
        genres: List of genre strings.
        image_url: URL to poster or thumbnail.
        rating: (optional) Movie rating, defaults to "".
        plot: (optional) Short movie plot, defaults to "".

    Returns:
        True if added successfully, False otherwise.
    """
    data = load_movies()

    # Ensure section exists — create it if missing
    if section not in data:
        data[section] = []


    # Create new movie dictionary
    movie = {
        "id": new_id(section),
        "Name": name,
        "Released": released,
        "Rating": rating,
        "imdb_id": imdb_id,
        "Genres": genres,
        "plot": plot,
        "Image": image_url,
        "Runtime": runtime,
        "User_rating": user_rating,
        "last_updated": datetime.now().isoformat()
    }

    # Add and save
    data[section].append(movie)
    save_movies(data)

    print(f"🎬 Added '{name}' to '{section}' section with id={movie['id']}.")
    return True

