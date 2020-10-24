import mysql.connector
from ._settings import MYSQL_ROOT_PASSWORD


class Database:
    def __init__(self):
        self._conn = mysql.connector.connect(
            host="127.0.0.1", user="root", password=MYSQL_ROOT_PASSWORD
        )
        cursor = self._conn.cursor()
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS starwars DEFAULT CHARACTER SET 'utf8'"
        )

    def __del__(self):
        self._conn.close()
        del self._conn
