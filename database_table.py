import sqlite3 as sql


conn = sql.connect("Contact.db")
cursor = conn.cursor()
table = cursor.execute(""" CREATE TABLE contact(
            name text,
            phone int,
            email text
            )
        """)
