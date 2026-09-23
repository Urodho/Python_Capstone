import sqlite3

def donation_report():
    Connection = sqlite3.connect("food_donation_system.db")
    
    cursor = connection.cursor()

    cursor.execute("""SELECT donors.name,donations.quantity,donations.expiry_date FROM donations
    JOIN donors ON donors ON donors.id = donations.donor_id""")

    records = cursor.fetchall()

    print("\n======DONATION REPORT======")

    for record in records:
        print("-------------------")
        print("Donor:", record[0])
        print("Food:", record[1])
        print("Quantity:", record[2])
        print("Expiry:", record[3])

    connection.close()    