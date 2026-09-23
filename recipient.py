import sqlite3

def add_recipient():
    connection = sqlite3.connect("food_donation_system.db")

    cursor = connection.cursor()

    name = input("Recipient name")
    location = input("location")

    cursor.execute(
        "INSERT INTO Recipients(name,location)VALUES(?,?)",
        (name,location)
    )


    connection.commit()
    connection.close()

    print("Recipient Registered")