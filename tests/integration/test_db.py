from unittest.mock import MagicMock, patch
import mysql.connector
import mysql.connector.errors
import pytest
from redhat_star_wars._database import Database


@patch("redhat_star_wars._database.sleep")
@patch(
    "redhat_star_wars._database.mysql.connector.connect",
    side_effect=[
        mysql.connector.errors.OperationalError(
            errno=2013,
            msg="2013 (HY000): Lost connection to MySQL server at 'reading initial communication packet', system error: 0",
            sqlstate="HY000",
        ),
        mysql.connector.errors.OperationalError(
            errno=2013,
            msg="2013 (HY000): Lost connection to MySQL server at 'reading initial communication packet', system error: 0",
            sqlstate="HY000",
        ),
        MagicMock(),
    ],
)
def test_waits_on_mysql_to_be_fully_operational(mock_connect, mock_sleep):
    Database()


@patch("redhat_star_wars._database.sleep")
@patch(
    "redhat_star_wars._database.mysql.connector.connect",
    side_effect=mysql.connector.errors.OperationalError(
        errno=2013,
        msg="2013 (HY000): Lost connection to MySQL server at 'reading initial communication packet', system error: 0",
        sqlstate="HY000",
    ),
)
def test_raises_runtime_exception_if_database_fails_to_connect_after_several_attempts(
    mock_connect, mock_sleep
):
    with pytest.raises(RuntimeError):
        Database()
    assert mock_connect.call_count == 10


def test_subsequent_connection_works_since_first_connection_populates_schemas():
    Database()
    Database()


def test_characters_already_cached_in_the_database_still_have_their_films_populated_when_returned():
    db = Database()
    cursor = db._conn.cursor()
    cursor.execute("DELETE FROM characters WHERE id = %s", (5,))

    character_uncached = db.get_character_by_id(5)
    character_cached = db.get_character_by_id(5)

    print(character_uncached, character_cached)
    assert character_uncached == character_cached
