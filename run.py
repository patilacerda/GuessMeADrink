import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import random
from colorama import Fore, Back, Style

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('cocktail_recipes')
RECIPES = SHEET.worksheet('recipes')

menu_art = '\033[34m' + """

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
""" + '\033[39m'


def calculate_age(birth_date):
    # Calculate the age based on the birth date.
    today = datetime.today()
    age = today.year - birth_date.year - (
            (today.month, today.day) < (birth_date.month, birth_date.day))
    return age


def select_random_cocktail():
    # Randomly select a row and column (cocktail) from the worksheet
    while True:
        random_row = random.randint(2, RECIPES.row_count)
        random_column = random.randint(2, len(spirit_categories) + 1)
        cocktail = RECIPES.cell(random_row, random_column).value
        if cocktail:
            return cocktail


print("Welcome to" + '\033[33m' + " Guess me a drink" + '\033[39m' + "!")
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
        print('\033[31m' + """
        Invalid date format. Please use the format dd/mm/yyyy.
        """ + '\033[39m')

if user_age < 18:
    print("You can drink a soda buddy ^-^")
else:
    print("Let's get started!")
    # Get the spirit category from the first row of the sheet
    spirit_categories = SHEET.sheet1.row_values(1)[1:]

    # Add "Random" as an option to select a random drink
    spirit_categories.append("I'm feeling lucky")

    while True:
        print('\033[33m' + "Choose a spirit category: " + '\033[39m')
        for i, category in enumerate(spirit_categories, start=1):
            # Main menu
            print(f"{i}. {category}")

        try:
            user_choice = int(input(
                "Enter the number of your chosen spirit category: \n"))
            if 1 <= user_choice <= len(spirit_categories):
                selected_category = spirit_categories[user_choice - 1]

                if selected_category == "I'm feeling lucky":
                    # Select a random cocktail
                    random_cocktail = select_random_cocktail()
                    print(f"Randomly selected cocktail: {random_cocktail}")
                    user_flavor_choice = input("""
                    Do you want to try another cocktail? (Y/N):\n
                    """).strip().upper()
                    if user_flavor_choice != "Y":
                        print("""
                        Enjoy your drinks wisely,
                        and don't forget to stay hydrated!
                        """)
                        break
                else:
                    # Get the available flavors
                    spirit_row = RECIPES.row_values(1)
                    spirit_index = spirit_row.index(selected_category)
                    flavors = RECIPES.col_values(1)
                    flavors = flavors[1:]  # Skip the header
                    # Show the flavor options to the user
                    print('\033[33m' + "Choose a flavor:" + '\033[39m')
                    for i, flavor in enumerate(flavors, start=1):
                        print(f"{i}. {flavor}")
                    user_flavor_choice = int(input(
                        "Enter the number of your chosen flavor: \n"))
                    if 1 <= user_flavor_choice <= len(flavors):
                        selected_flavor = flavors[user_flavor_choice - 1]

                        # Find the row index of the selected spirit
                        spirit_index = spirit_categories.index(
                            selected_category)

                        # Return the recipe
                        recipe = RECIPES.cell(
                            user_flavor_choice + 1, spirit_index + 2).value

                        print("You selected a: " + '\033[33m' + f"""
                        {selected_category} - {selected_flavor} cocktail.""")
                        print('\033[39m')
                        print(f"Here's your recipe:\n{recipe}")
                        user_flavor_choice = input("""
                        Do you want to try another cocktail? (Y/N): \n
                        """).strip().upper()
                        if user_flavor_choice != "Y":
                            print('\033[33m' + """
                            Enjoy your drinks wisely,
                            and don't forget to stay hydrated!
                            """ + '\033[39m')
                            break
                    else:
                        print('\033[31m' + """
                        Invalid flavor selection. Please choose a valid flavor.
                        """ + '\033[39m')
            else:
                print('\033[31m' + """
                Invalid selection. Please choose a valid spirit category.
                """ + '\033[39m')
        except ValueError:
            print('\033[31m' + """
            Invalid input. Please enter a valid number.
            """ + '\033[39m')
