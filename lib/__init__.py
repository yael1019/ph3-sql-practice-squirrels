import sqlite3

CONN = sqlite3.connect('lib/db/development.db')
CURSOR = CONN.cursor()

# BELOW ARE SQL COMMANDS THAT WILL CREATE THE TABLE #

create_squirrels_sql = """CREATE TABLE IF NOT EXISTS squirrels (
id INTEGER PRIMARY KEY,
name TEXT,
num_acorns INT,
rabid BOOLEAN
)
"""

CURSOR.execute(create_squirrels_sql)
