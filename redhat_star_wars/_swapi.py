import random
from urllib.parse import urljoin
import requests

SWAPI_URL = "https://swapi.dev/api/"


def get_character_count():
    """Get the total number of characters from swapi.

    This is useful later when grabbing individual character ids to avoid out-of-bounds."""
    resp = requests.get(urljoin(SWAPI_URL, "people/"))
    json = resp.json()
    return json["count"]


def gen_random_character_ids(amount):
    """Generates `amount` character ids, ranging from 1 to however many characters are in swapi."""
    count = get_character_count()
    for _ in range(amount):
        yield random.randint(1, count)


def get_character_by_id(id):
    """Returns swapi's json for an individual character."""
    resp = requests.get(urljoin(SWAPI_URL, "people/{id}/".format(id=id)))
    json = resp.json()
    if json.get("detail", None) == "Not found":
        raise KeyError(f"Character #{id} does not have any details.")
    return json


def get_film_by_id(id):
    """Returns swapi's json for an individual film."""
    resp = requests.get(urljoin(SWAPI_URL, "films/{id}/".format(id=id)))
    json = resp.json()
    return json
