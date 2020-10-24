import json
from ._database import Database


def main():
    db = Database()
    films = db.get_films()
    print(json.dumps(films, indent=4))


if __name__ == "__main__":
    main()
