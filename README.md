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

When you are satisfied, you can stop any running dockers with:

```
make teardown
```

### Future Improvements
* Adding some configuration options other than a hard-coded database connection to `localhost:3306` with a password that has to be stored in a `.env` file.
* Configuring `task_one.py` as an entry point in `pyproject.toml`. Perhaps giving it a more descriptive name (random_star_wars_json?).
