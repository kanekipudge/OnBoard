import sqlite3

with sqlite3.connect('../ONboard.db') as database:
    cursor = database.cursor()

    query = """  CREATE TABLE IF NOT EXISTS users_data(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        surname TEXT,
        lastname TEXT,
        email TEXT,
        phone_number TEXT,
        password TEXT,
        rating INTEGER,
        checkpoint INTEGER DEFAULT 1
        )  """
    query1 = """    CREATE TABLE IF NOT EXISTS test_data()"""
    cursor.execute(query)

with sqlite3.connect('../ONboard.db') as database:
    cursor = database.cursor()

    query = """  CREATE TABLE IF NOT EXISTS tests_data(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        surname TEXT,
        lastname TEXT,
        email TEXT,
        phone_number TEXT,
        password TEXT,
        rating INTEGER,
        checkpoint INTEGER
        )  """

    cursor.execute(query)


