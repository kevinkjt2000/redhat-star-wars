from unittest.mock import patch
import pytest
from redhat_star_wars._swapi import (
    get_character_by_id,
    get_character_count,
    gen_random_character_ids,
)


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


@patch("redhat_star_wars._swapi.get_character_count", return_value=20)
def test_random_number_generation_is_based_on_the_number_of_characters_from_swapi(
    mock_swapi,
):
    for character_id in gen_random_character_ids(1000):
        assert 1 <= character_id and character_id <= mock_swapi.return_value


@pytest.mark.vcr
def test_characters_detail_not_found_raises_exception():
    with pytest.raises(KeyError):
        get_character_by_id(17)
