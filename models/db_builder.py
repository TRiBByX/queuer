import os
import sqlite3

debug = True


def db_exists():
    return 'queuer.db' in os.listdir('db/')


def db_populate():
    pass


def db_build():
    # Builds 1 database with three tables.
    # Archive:
    #   Previously run jobs.
    # Scripts:
    #   The scripts/functionality bank.
    # Queue:
    #   The queue of jobs.
    if db_exists() is False:
        print('running...')
        conn = sqlite3.connect('db/queuer.db')
        sql = '''CREATE TABLE queue(id INTEGER PRIMARY KEY autoincrement,
                                    jobname TEXT, parameters TEXT, time DATE,
                                    status TEXT)'''
        db_executer(sql)
        sql = '''CREATE TABLE scripts(id INTEGER PRIMARY KEY autoincrement,
                                     name TEXT,
                                     code TEXT,
                                     author TEXT,
                                     params TEXT)'''
        db_executer(sql)
        sql = '''CREATE TABLE archive(id INTEGER PRIMARY KEY autoincrement,
                                    jobname TEXT,
                                    parameters TEXT,
                                    time DATE,
                                    status TEXT)'''
        db_executer(conn, sql)


def db_executer(conn, sql):
    conn.execute(sql)
    conn.commit()


if __name__ == '__main__' and debug is True:
    db_build()
