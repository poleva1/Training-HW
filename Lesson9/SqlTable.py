from sqlalchemy import create_engine
from sqlalchemy.sql import text

class SqlTable:
    scripts = {
        "select": "select * from places",
        "select by id": text("select * from places where place_id =:select_id"),
    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_places(self):
        return self.db.execute(self.scripts("select")).fetchall()

    def get_place_by_id(self, id):
        return self.db.execute(self.scripts("select by id"), select_id=id).fetchall()
