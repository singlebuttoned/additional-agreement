import sqlite3 as sq
from pathlib import Path


class DB:
    def __init__(self):
        self.db_path = str(Path("core/database/data/db.db"))
        self.connection = sq.connect(self.db_path, check_same_thread=False)
        self.cursor = self.connection.cursor()
