from sqlalchemy import create_engine
from sqlalchemy.sql import text
from SqlTable import SqlTable

db_connection_string = "postgresql://postgres:777@localhost:5432/QA"
db = create_engine(db_connection_string)

def test_db_connection():
    names = db.table_names()
    assert names[14] == 'places'

def test_select():
    rows = db.execute("select * from places").fetchall()
    row1 = rows[0]
    assert row1["place_id"] == 1
    assert row1["place_name"] == "дом"

def test_select_one_row_with_two_filters():
    sql_statement = text("select from places where place_id >= :place_id and place_size > :place_size")
    my_params = {
        'place_id': 1,
        'place_size': 0
    }
    rows = db.execute(sql_statement, my_params).fetchall()
    assert len(rows) == 3

