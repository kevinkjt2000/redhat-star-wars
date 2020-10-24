import pytest
from redhat_star_wars._swapi import get_character_by_id, get_character_count


@pytest.mark.vcr
def test_character_count_is_based_from_api_data():
    count = get_character_count()
    assert count == 82  # expected number comes from the cassette file


@pytest.mark.vcr
def test_json_dict_is_returned_when_fetching_characters_by_id():
    character = get_character_by_id(1)
    assert character["name"] == "Luke Skywalker"
    character = get_character_by_id(82)
    assert character["films"] == [
        "http://swapi.dev/api/films/5/",
        "http://swapi.dev/api/films/6/",
    ]
