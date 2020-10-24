import json
from unittest.mock import patch
from redhat_star_wars.task_one import main, _get_random_character_ids


def test_output_matches_expected_shape(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == json.dumps([{}], indent=4) + "\n"


@patch("redhat_star_wars.task_one.get_character_count", return_value=20)
def test_random_number_generation_is_based_on_the_number_of_characters_from_swapi(
    mock_swapi,
):
    for character_id in _get_random_character_ids(1000):
        assert 1 <= character_id and character_id <= mock_swapi.return_value
