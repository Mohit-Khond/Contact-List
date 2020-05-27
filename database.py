import sqlite3 as sql
import cmds


def insert_into_db():
    conn = sql.connect("Contact.db")
    cursor = conn.cursor()
    data_args = [(cmds.details())]
    insert_data = cursor.executemany("INSERT INTO contact VALUES (?,?,?)", data_args)
    conn.commit()
    conn.close()
    return


insert_into_db()



