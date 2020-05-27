import sqlite3


def view_full_db():
    conn = sqlite3.connect("Contact.db")
    cursor = conn.cursor()
    data = cursor.execute("SELECT * FROM contact")
    all_data = data.fetchall()
    conn.close()
    return all_data


def view_one():
    conn = sqlite3.connect("Contact.db")
    cursor = conn.cursor()
    data = cursor.execute("SELECT * FROM contact")
    first_entry = data.fetchone()
    conn.close()
    return first_entry


def view_many():
    show_data = int(input("Enter the number of data you want to look at: "))
    conn = sqlite3.connect("Contact.db")
    cursor = conn.cursor()
    data = cursor.execute("SELECT * FROM contact")
    data_view = data.fetchmany(show_data)
    conn.close()
    return data_view


user_input = input("""Enter your choice among this :-
        1. View Full Database
        2. View the first Entry
        3. View some entries
    ---> """)
if int(user_input) == 1:
    print(view_full_db())
elif int(user_input) == 2:
    print(view_one())
elif int(user_input) == 3:
    print(view_many())
else:
    print("Enter one of the choice")
