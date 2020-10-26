from time import sleep
import mysql.connector
from ._settings import MYSQL_ROOT_PASSWORD
from ._swapi import get_character_by_id, get_film_by_id


class Database:
    def __init__(self):
        for attempt in range(10):
            try:
                self._conn = mysql.connector.connect(
                    host="127.0.0.1", user="root", password=MYSQL_ROOT_PASSWORD
                )
                break
            except mysql.connector.errors.OperationalError as exc:
                if exc.errno == mysql.connector.errorcode.CR_SERVER_LOST:
                    sleep(3)
                    continue
                else:
                    # I would test this branch, but ficticiously making up an
                    # OperationalError with a different code seems wrong
                    # somehow. I'd want to properly research a code that could
                    # happen in practice.
                    raise exc
        else:
            raise RuntimeError("Unable to connect to MySQL database.")

        cursor = self._conn.cursor()
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS starwars DEFAULT CHARACTER SET 'utf8'"
        )
        cursor.execute("USE starwars")
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS characters (
                id INT NOT NULL PRIMARY KEY,
                name VARCHAR(30) NOT NULL
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS films (
                id INT NOT NULL PRIMARY KEY,
                title VARCHAR(30) NOT NULL
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS character_films (
                character_id INT,
                film_id INT,
                CONSTRAINT FOREIGN KEY (character_id) REFERENCES characters (id) ON DELETE CASCADE ON UPDATE CASCADE,
                CONSTRAINT FOREIGN KEY (film_id) REFERENCES films (id) ON DELETE CASCADE ON UPDATE CASCADE
            )
            """
        )
        self._conn.commit()
        cursor.close()

    def __del__(self):
        self._conn.close()
        del self._conn

    def get_character_by_id(self, id):
        cursor = self._conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM characters WHERE id = %s", (id,))
        row = cursor.fetchone()
        if row == None:
            character = get_character_by_id(id)
            character_data = {
                "id": id,
                "name": character["name"],
            }
            cursor.execute(
                "INSERT INTO characters (id, name) VALUES (%(id)s, %(name)s)",
                character_data,
            )
            self._conn.commit()

            character_data["films"] = set()
            for film_url in character["films"]:
                # each film url ends with the id followed by a slash
                film_id = film_url.split("/")[-2]
                film = self.get_film_by_id(film_id)
                cursor.execute(
                    "INSERT INTO character_films (character_id, film_id) VALUES (%s, %s)",
                    (id, film_id),
                )
                character_data["films"].add(film["title"])
            self._conn.commit()
            character_data["films"] = sorted(character_data["films"])

            return character_data
        else:
            cursor.execute(
                """
                SELECT films.title
                FROM character_films
                INNER JOIN films
                ON character_films.character_id = %s
                AND character_films.film_id = films.id
                """,
                (id,),
            )
            row["films"] = sorted([film["title"] for film in cursor])
        return row

    def get_film_by_id(self, id):
        cursor = self._conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM films WHERE id = %s", (id,))
        row = cursor.fetchone()
        if row == None:
            film = get_film_by_id(id)
            film_data = {
                "id": id,
                "title": film["title"],
            }
            cursor.execute(
                "INSERT INTO films (id, title) VALUES (%(id)s, %(title)s)",
                film_data,
            )
            self._conn.commit()
            return film_data
        return row
