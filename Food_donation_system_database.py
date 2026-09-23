import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

connection = sqlite3.connect("food_donation_system.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS donors(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
phone TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS donations(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
food_name TEXT,
quantity INTEGER,
expiry_date TEXT,
donor_id INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS recipients(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
location TEXT
)
""")

# ADD THE USER TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE,
password TEXT
)
""")

# INSERT THE DEFAULT ADMIN USER
admin_user = os.getenv("ADMIN_USER", "admin")
admin_pass = os.getenv("ADMIN_PASSWORD")

cursor.execute(
    "INSERT OR IGNORE INTO users(username, password)VALUES(?,?)",
    (admin_user, admin_pass)
)

connection.commit()
connection.close()

print("Database Created Successfully")
