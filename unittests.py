import unittest
import os
import sqlite3
from models import db_builder


class DB_tests(unittest.TestCase):

    def test_db_exists(self):
        if 'queuer.db' in os.listdir('db/'):
            self.assertTrue(db_builder.db_exists())
        else:
            self.assertFalse(db_builder.db_exists())

    def test_db_builder(self):
        if 'queuer.db' not in os.listdir('db/'):
            db_builder.db_build()

        conn = sqlite3.connect('db/queuer.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        tables = list(map('_'.join, tables))
        for table in ['queue', 'scripts', 'archive']:
            if table not in tables:
                test = False
            else:
                test = True
        self.assertTrue(test)


if __name__ == '__main__':
    unittest.main(verbosity=2)
