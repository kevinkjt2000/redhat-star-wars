import json
import random
from ._database import Database
from ._swapi import get_character_count


def _get_random_character_ids(amount):
    """Generates `amount` character ids, ranging from 1 to however many characters are in swapi."""
    count = get_character_count()
    for _ in range(amount):
        yield random.randint(1, count)


def main():
    db = Database()
    films = db.get_films()
    print(json.dumps(films, indent=4))


if __name__ == "__main__":
    main()
