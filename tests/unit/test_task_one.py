import json
from unittest.mock import patch
import pytest
from redhat_star_wars.task_one import main


@pytest.mark.vcr
@patch("redhat_star_wars.task_one.gen_random_character_ids", return_value=[1, 82])
def test_output_matches_expected_shape(mock_gen_char_ids, capsys):
    main()
    captured = capsys.readouterr()
    assert (
        captured.out
        == json.dumps(
            [
                {
                    "film": "A New Hope",
                    "characters": ["Luke Skywalker"],
                },
                {"film": "Attack of the Clones", "characters": ["Sly Moore"]},
                {"film": "Return of the Jedi", "characters": ["Luke Skywalker"]},
                {
                    "film": "Revenge of the Sith",
                    "characters": ["Luke Skywalker", "Sly Moore"],
                },
                {"film": "The Empire Strikes Back", "characters": ["Luke Skywalker"]},
            ],
            indent=4,
        )
        + "\n"
    )


@pytest.mark.vcr
@patch("redhat_star_wars.task_one.gen_random_character_ids", return_value=[1, 1])
def test_duplicate_random_characters_only_appear_once_in_output(
    mock_gen_char_ids, capsys
):
    main()
    captured = capsys.readouterr()
    assert (
        captured.out
        == json.dumps(
            [
                {
                    "film": "A New Hope",
                    "characters": ["Luke Skywalker"],
                },
                {"film": "Return of the Jedi", "characters": ["Luke Skywalker"]},
                {
                    "film": "Revenge of the Sith",
                    "characters": ["Luke Skywalker"],
                },
                {"film": "The Empire Strikes Back", "characters": ["Luke Skywalker"]},
            ],
            indent=4,
        )
        + "\n"
    )


@pytest.mark.vcr
@patch(
    "redhat_star_wars.task_one.gen_random_character_ids", return_value=[17, 17, 17, 17]
)
def test_all_random_ids_lack_details(mock_gen_char_ids, capsys):
    """In practice, this will rarely happen, but it could happen."""
    main()
    captured = capsys.readouterr()
    assert captured.out == json.dumps([], indent=4) + "\n"
