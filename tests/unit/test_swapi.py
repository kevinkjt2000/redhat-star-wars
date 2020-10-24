import pytest
from redhat_star_wars._swapi import get_character_count


@pytest.mark.vcr
def test_character_count_is_based_from_api_data():
    count = get_character_count()
    assert count == 82  # expected number comes from the cassette file
