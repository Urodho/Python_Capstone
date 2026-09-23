def dashboard():
    connection = sqlite3.connect("food_donation_system.db")
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM donors")
    donors = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM donations")
    donations = cursor.fetchonel()[0]

    cursor.execute("SELECT COUNT(*) FROM donations")
    donations = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM recipients")
    recipients = cursor.fetchone()[0]

    print("\n======DASHBOARD=====")
    print("Total Donors:", donors)
    print("Total Donations:", donations)
    print("Total Recipients:", recipients)

    connection.close()