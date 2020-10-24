from urllib.parse import urljoin
import requests

SWAPI_URL = "https://swapi.dev/api/"


def get_character_count():
    """Get the total number of characters from swapi.

    This is useful later when grabbing individual character ids to avoid out-of-bounds."""
    resp = requests.get(urljoin(SWAPI_URL, "people/"))
    json = resp.json()
    return json["count"]
