import json
import random
from ._database import Database
from ._swapi import get_character_count


def _gen_random_character_ids(amount):
    """Generates `amount` character ids, ranging from 1 to however many characters are in swapi."""
    count = get_character_count()
    for _ in range(amount):
        yield random.randint(1, count)


def main():
    db = Database()

    characters = []
    for character_id in _gen_random_character_ids(15):
        characters.append(db.get_character_by_id(character_id))

    films = {}
    for character in characters:
        for film in character["films"]:
            if film not in films:
                films[film] = {"characters": []}
            films[film]["characters"].append(character["name"])

    film_list = [
        {"film": film, "character": sorted(list(films[film]["characters"]))}
        for film in sorted(films.keys())
    ]
    print(json.dumps(film_list, indent=4))


if __name__ == "__main__":
    main()
