from datetime import datetime

# Define drink recipes using dictionaries
drink_recipes = {
    'gin': {
        'citric': 'Gin and Tonic',
        'berry': 'Bramble',
        'sour': 'Gimlet',
        'spicy': 'Negroni',
        'herbal': 'Martini',
        'sweet': 'Tom Collins',
        'dry': 'Martini',
        'creamy': 'Ramos Gin Fizz',
        'fizzy': 'Gin Fizz'
    },
    'vodka': {
        'citric': 'Screwdriver',
        'berry': 'Cosmopolitan',
        'sour': 'Lemon Drop',
        'spicy': 'Bloody Mary',
        'herbal': 'Moscow Mule',
        'sweet': 'Sex on the Beach',
        'dry': 'Vodka Martini',
        'creamy': 'White Russian',
        'fizzy': 'Vodka Soda'
    },
    'whisky': {
        'citric': 'Whiskey Sour',
        'berry': 'Blackberry Whiskey Smash',
        'sour': 'Sazerac',
        'spicy': 'Hot Toddy',
        'herbal': 'Mint Julep',
        'sweet': 'Boulevardier',
        'dry': 'Manhattan',
        'creamy': 'Whiskey Cream Soda',
        'fizzy': 'Whiskey Highball'
    },
    'rum': {
        'citric': 'Daiquiri',
        'berry': 'Mai Tai',
        'sour': 'Zombie',
        'spicy': 'Rum Punch',
        'herbal': 'Rum Swizzle',
        'sweet': 'Pina Colada',
        'dry': 'El Presidente',
        'creamy': 'Coquito',
        'fizzy': 'Rum and Coke'
    },
    'tequila': {
        'citric': 'Margarita',
        'berry': 'Tequila Sunrise',
        'sour': 'Paloma',
        'spicy': 'Bloody Maria',
        'herbal': 'Agave Old Fashioned',
        'sweet': 'Tequila Mockingbird',
        'dry': 'Tequila Gimlet',
        'creamy': 'Batanga',
        'fizzy': 'Tequila Soda'
    },
    'I\'m feeling lucky': None
}

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
while input("Press Enter to start...") != "":
    pass

# Verify the age of the user
while True:
    user_age_str = input("Please enter your date of birth (dd/mm/yyyy): ")
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
