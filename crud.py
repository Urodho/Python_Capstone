import sqlite3
# view all donors
def view_donors():

    connection = sqlite3.connect("food_donation_system.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM donors")
                   
    donors = cursor.fetchall()

    if len(donors) == 0:
        print("No donors found.")
    else:
        for donors in donors:
         print(donor)

    connection.close()

# search donor
def search_donor():

    connection = sqlite3.connect("food_donation system.db")
    cursor = connection.cursor

    donor_id = input("Enter Donor ID")

    cursor.execute("SELECT * FROM donors WHERE id=?", (donor_id,))

    donor = cursor.fetchone()

    if donor:
      print(donor)
    else:
      print("Donor not found.")  
    connection.close()  

# Update donor
def update_donor():
    connection = sqlite3.connect("food_donation_system.db")

    cursor = connection.cursor()

    donor_id = input("Enter donor ID")
    phone = input("Enter new phone number")

    cursor.execute("UPDATE donors SET phone=? WHERE id=?",(new_phone,donor_id))

    connection.commit()

    print("Donor updated successfullly")

    connection.close()

    #Delete donor
def delete_donor():

    connection = sqlite3.connect("food_donation_system.db")

    cursor = connection.cursor()

    donor_id = input("Enter donor ID to delete")

    cursor.execute("DELETE FROM donors WHERE id=?",)

    connection.commit()

    
    print("Donor deleted successfully.")

    connection.close()






