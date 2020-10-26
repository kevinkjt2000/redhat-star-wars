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
                    "character": ["Luke Skywalker"],
                },
                {"film": "Attack of the Clones", "character": ["Sly Moore"]},
                {"film": "Return of the Jedi", "character": ["Luke Skywalker"]},
                {
                    "film": "Revenge of the Sith",
                    "character": ["Luke Skywalker", "Sly Moore"],
                },
                {"film": "The Empire Strikes Back", "character": ["Luke Skywalker"]},
            ],
            indent=4,
        )
        + "\n"
    )
