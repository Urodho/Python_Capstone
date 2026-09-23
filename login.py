import sqlite3

def login():

    connection = sqlite3.connect("food_donation_system.db")
    cursor = connection.cursor()

    username = input("Username:")
    password = input("Password:")

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",(username, password))

    user = cursor.fetchone()

    if user:
        print("Login Successfull!")
        return True
    else:
        print("invalid username or password!")
        return False