import json
from redhat_star_wars._database import Database
from redhat_star_wars._swapi import gen_random_character_ids


def main():
    """See README.md for detailed description of task_one.py."""
    db = Database()

    characters = [db.get_character_by_id(id) for id in gen_random_character_ids(15)]

    films = {}
    for character in characters:
        for film in character["films"]:
            if film not in films:
                films[film] = {"characters": []}
            films[film]["characters"].append(character["name"])

    film_list = [
        # It bothers me a little that character was not plural in the
        # instructions, so I changed it to be plural
        {"film": film, "characters": sorted(set(films[film]["characters"]))}
        for film in sorted(films.keys())
    ]
    print(json.dumps(film_list, indent=4))


if __name__ == "__main__":
    main()
