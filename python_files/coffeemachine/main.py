MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

COIN_VALUE = {"quarters": 0.25, "dimes": 0.1, "nickles": 0.05, "pennies": 0.01}

def is_resource_sufficient(ingredients: dict[str, int], resources_avail: dict[str, int]) -> bool:
    """Return True if every ingredient is in stock, otherwise report the first shortage."""
    for item, amount in ingredients.items():
        if resources_avail[item] < amount:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins() -> float:
    """Prompt for each coin type and return the total inserted, rounded to cents."""
    print("Please insert coins.")
    total = 0.0
    for coin, value in COIN_VALUE.items():
        total += int(input(f"How many {coin}?: ")) * value
    return round(total, 2)

def is_transaction_successful(payment_amount: float, drink_cost: float) -> bool:
    """Return True when payment_amount is accepted, otherwise False if money is insufficient."""
    if payment_amount >= drink_cost:
        change = round(payment_amount - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(coffee_type: str, menu_ingredients: dict[str, int], resource_avail: dict[str, int]) -> None:
    """Deduct the required ingredients from the resources."""
    for item, amount in menu_ingredients.items():
        resource_avail[item] -= amount
    print(f"Here is your {coffee_type} ☕. Enjoy!")


def make_report(resource_detail: dict[str, int]) -> None:
    """Print a report of available ingredients and profit made."""
    print(f"Water: {resource_detail['water']}ml")
    print(f"Milk: {resource_detail['milk']}ml")
    print(f"Coffee: {resource_detail['coffee']}g")
    print(f"Money: ${profit}")

ready = True

while ready:
    request = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    if request in MENU:
        drink = MENU[request]
        if is_resource_sufficient(drink['ingredients'], resources):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(request, drink["ingredients"], resources)
    elif request == "report":
        make_report(resource_detail=resources)
    elif request == "off":
        ready = False
    else:
        print("Sorry that's not a valid option.")