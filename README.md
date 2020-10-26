# RedHat Technical Assessment - Star Wars
This is a project I wrote during a weekend to show that I know a few of the common technologies used in a role I interviewed for. Inside, one will find python3, docker, mysql, API calls to https://swapi.dev/, test coverage, and some other things that I found time for. Approximately 11 hours spent on this, according to my measurements from https://wakatime.com.

### Usage
The main script for completing the assignment is `task_one.py`. It is responsible for taking JSON data from SWAPI then caching character names, film titles, and their relation into MySQL. This data is use to print JSON of 15 random characters with the film titles that they participated in. Here is the general shape of the output:

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
make bootstrap  # In theory, this needs to be run only once. In practice, I used it to wipe the database.
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

![image](https://user-images.githubusercontent.com/4098674/97135290-de89df00-171d-11eb-9141-160ba2876dce.png)

### Future Improvements
* Adding some configuration options other than a hard-coded database connection to `localhost:3306` with a password that has to be stored in a `.env` file.
* Configuring `task_one.py` as an entry point in `pyproject.toml`. Perhaps giving it a more descriptive name (random_star_wars_json?).
* Run `make test` in a CI job and only allow PRs that pass that job to be merged to master branch. Along these same lines, upload coverage to codecov and include that in the branch protection strategy.
* Utilize sqlalchemy to shorten SQL boiler-plate code.
* Add pylint between black formatting and pytest in `make test`, and deal with the fallout of tons of frivilous defaults that need to be tweaked to get a passing linter.
* Reach 100% test coverage. 90% is good, but 100% is empirically better. And without the empire, Star Wars would be missing stories.
* Cool README badges! The ones that show CI is passing, supported python versions, pypi version, code coverage, etc.
* Run python/poetry from a docker in development. This would make it so that the only dev tools required would be make, docker, and docker-compose. Personally, I use asdf-python to manage multiple versions of python on my system. If others on the team liked that, I would document going that route instead.
* Separate development database from test database. Make it easier to drop certain records from either of these aside from running `make bootstrap` to completely wipe docker volumes.
