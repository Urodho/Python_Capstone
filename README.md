
# Food Donation Management System

A command-line Python application that helps manage food donations. It keeps track of donors, donations and recipients, flags expired food, and produces donation reports. Data is stored in a local SQLite database.

## Features

- Login system (admin account)
- Add, view, search, update and delete donors
- Record food donations (name, quantity, expiry date, donor)
- Add recipients
- Check for expired food
- Generate donation reports

## Tech Stack

- Python 3
- SQLite (`sqlite3`)
- `python-dotenv` for environment variables

## Project Structure

```
Python_Capstone/
├── main.py                            # Menu and program entry point
├── Food_donation_system_database.py   # Creates the database and tables
├── login.py                           # Login logic
├── donor.py                           # Add donor
├── donation.py                        # Add donation, check expired food
├── recipient.py                       # Add recipient
├── crud.py                            # View, search, update, delete donors
├── reports.py                         # Donation report
├── requirements.txt
└── README.md
```

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Urodho/Python_Capstone.git
   cd Python_Capstone
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS / Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the project folder:
   ```
   ADMIN_USER=admin
   ADMIN_PASSWORD=choose_a_strong_password
   ```
   The `.env` file is ignored by Git and is never uploaded.

5. **Create the database** (run once):
   ```bash
   python Food_donation_system_database.py
   ```

6. **Run the app**
   ```bash
   python main.py
   ```

## Usage

Log in with the admin username and the password you set in `.env`, then choose an option from the menu, for example:

| Option | Action |
|--------|--------|
| 1 | Add donor |
| 2 | Add donation |
| 3 | Add recipient |
| 4 | View donors |
| 5 | Search donor |
| 6 | Update donors|
| 7 | Delete donor |
| 8 | Check Expired Food |
| 9 | Donation report |
| 10 | Exit |

## Known Limitations

- Passwords are stored as plain text in the database. A production system should hash them (for example with `bcrypt`).
- This is a command-line app with no graphical interface.

## Author

Urodho