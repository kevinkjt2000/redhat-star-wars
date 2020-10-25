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


def test_subsequent_connection_works_since_first_connection_populates_schemas():
    Database()
    Database()
