from redhat_star_wars._database import Database


def test_connection_works():
    db = Database()


def test_subsequent_connection_works_since_first_connection_populates_schemas():
    db = Database()
    db = Database()
