import json
from redhat_star_wars.task_one import main


def test_output_matches_expected_shape(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == json.dumps([{}], indent=4) + "\n"
