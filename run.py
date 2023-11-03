import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('cocktail_recipes')

menu_art = """

                    ████████████████████████████████████
                    ██░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░██
                      ██      ██                    ██
                        ██      ██                ██
                          ██      ░░░░          ██
                            ██    ░░██        ██
                              ██      ██    ██
                                ██        ██
                                  ██    ██
                                    ████
                                    ████
                                    ████
                                    ████
                                    ████
                                    ████
                                    ████
                                  ████████
                                ████████████
                            ▓▓▓▓████████████▓▓██
"""


def calculate_age(birth_date):
    """
    Calculate the age based on the birth date.
    """
    today = datetime.today()
    age = today.year - birth_date.year - (
            (today.month, today.day) < (birth_date.month, birth_date.day))
    return age


print("Welcome to Guess me a drink")
print(menu_art)

# Wait for the user to press Enter
while input("Press Enter to start...\n") != "":
    pass

# Verify the age of the user
while True:
    user_age_str = input("Please enter your date of birth (dd/mm/yyyy): \n")
    try:
        user_age_date = datetime.strptime(user_age_str, "%d/%m/%Y")
        user_age = calculate_age(user_age_date)
        break
    except ValueError:
        print("Invalid date format. Please use the format dd/mm/yyyy.")

if user_age < 18:
    print("You can drink a soda buddy ^-^")
else:
    print("Let's get started!")
