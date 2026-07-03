import random

BAD_DRINKS = {
    "Coca-Cola": 39,
    "Monster": 54,
    "Gatorade": 34
}

GOOD_DRINKS = {
    "Sparkling Water": 0,
    "Black Coffee": 0,
    "Coconut Water": 9
}

def check_beverage(drink_name: str) -> str:
    """Checks if a drink is in the BAD_DRINKS database, returns its sugar content

    and recommends a healthier alternative from GOOD_DRINKS.
    """
    if drink_name in BAD_DRINKS:
        sugar = BAD_DRINKS[drink_name]
        recommendation = random.choice(list(GOOD_DRINKS.keys()))
        return f"{drink_name} has {sugar}g of sugar. We recommend trying {recommendation} instead!"
    
    return "Drink not found in database."
