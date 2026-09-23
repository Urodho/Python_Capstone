import sqlite3
from datetime import datetime

def add_donation():

    connection = sqlite3.connect("food_donation_system.db")
    cursor = connection.cursor()

    food_name = input ("Enter food name")
    quantity = int(input("Enter quantity"))
    expiry_date = input("Enter expiry date (YYYY-MM-DD):")
    donor_id = int(input("Enter donor ID:"))

    cursor.execute(
        "INSERT INTO donations(food_name,quantity, expiry_date, donor_id) VALUES(?, ?, ?, ?)",
        (food_name, quantity, expiry_date, donor_id)
    )

    connection.commit()
    connection.close()

    print("Donation added successfully")


def check_expired_food():
    connection = sqlite3.connect("food_donation_system.db")
    cursor = connection.cursor()

    cursor.execute("SELCT food_name, expiry_date FROM donations")

    foods = cursor.fetchall()

    today = datetime.today().date()

    print("\n======EXPIRY CHECKER======") 

    for food in foods:

        food_name = food[0]
        expiry = datetime.strptime(food[1],
"%Y-%m-%d").date()

        if expiry < today:
            print(f"{food_name}--> EXPIRED")
        else:
            print(f"{food_name}--> SAFE")

    connection.close()

