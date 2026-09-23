import sqlite3
def add_donor():

    connection = sqlite3.connect("food_donation_system.db")

    cursor = connection.cursor()

    name = input("Enter donor name")
    phone = input("Enter donor phone")

    cursor.execute(
        "INSERT INTO donors(name,phone)VALUES(?,?)",
        (name,phone)   
    )

    connection.commit()
    connection.close()

    print("Donor added successfully.")
    
    