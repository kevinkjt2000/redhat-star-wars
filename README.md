# RedHat Technical Assessment - Star Wars
This is a project I wrote during a weekend to show that I know a few of the common technologies used in a role I interviewed for. Inside, one will find python3, docker, mysql, API calls to https://swapi.dev/, test coverage, and some other things that I found time for.

### Usage
The main script for completing the assignment is `task_one.py`. It is responsible for storing raw API data from swapi into MySQL, and then printing JSON data of 15 random characters with the film titles that they participated in. Here is the general shape of the output:

```
$ make run
[
    {
        "film": "The Empire Strikes Back",
        "character":
        [
            "Luke Skywalker",
            "C-3PO",
            ...
        ]
    },
    ...
    {
        "film": "Return of the Jedi",
        "character":
        [
            ...
        ]
    }
]
```

### Contributing
Install python3.8, poetry, docker, GNU Make, and docker-compose. Use the following to test your changes:

```
make bootstrap  # in theory, this needs to be run only once
make test
```

The first test run may take several seconds longer due to waiting on MySQL to start properly. Subsequent test runs should happen much faster.

If you do not have a plugin in your text editor that automatically uses black from poetry's virtual environment, you may want to run format before test:

```
make format test
```

You may notice vcr cassette errors if any network interactions are modified. Simply remove the offending cassette yaml file, and rerun the tests to generate a new one. Any network interacting test should have an associated cassette file by using the pytest vcr marker. This allows for running the tests when not connected to the Internet.

When you are satisfied, you can stop any running dockers with:

```
make teardown
```

### Future Improvements
* Adding some configuration options other than a hard-coded database connection to `localhost:3306` with a password that has to be stored in a `.env` file.
* Configuring `task_one.py` as an entry point in `pyproject.toml`. Perhaps giving it a more descriptive name (random_star_wars_json?).
* Run `make test` in a CI job and only allow PRs that pass that job to be merged to master branch.
* Utilize sqlalchemy to shorten SQL boiler-plate code.
* Add pylint between black formatting and pytest in `make test`, and deal with the fallout of tons of frivilous defaults that need to be tweaked to get a passing linter.
