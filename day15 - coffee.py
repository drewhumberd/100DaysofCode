'''Operates the coffee machine.'''

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

COINS = {
  "quarter": .25,
  "dime": .10,
  "nickel": .05,
  "penny": .01
}

def charge_customer(drink, quarters, dimes, nickels, pennies):
    '''Calculates whether payment is sufficient and determines change if necessary.'''
    total_paid = ((quarters * COINS["quarter"]) + (dimes * COINS["dime"]) +
                  (nickels * COINS["nickel"]) + (pennies * COINS["penny"]))
    fix_total = float(f"{total_paid:0.2f}")
    drink_cost = MENU[drink]["cost"]
    if fix_total > drink_cost:
        resources["money"] += drink_cost
        return float(f"{(fix_total - drink_cost):0.2f}")
    elif fix_total < drink_cost:
        return "Insufficient funds."
    resources["money"] = drink_cost
    return

def use_ingredients(drink):
    '''Removes ingredients if drink is sold.'''
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]

def check_ingredients(drink):
    '''Checks for sufficient amounts of all ingredients.'''
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] < MENU[drink]["ingredients"][ingredient]:
            return f"Insufficient {ingredient}."
    return "Sufficient ingredients."


def run_machine():
    '''Runs the entire machine.'''
    request = input('''
Welcome to the coffee machine,
how can I help you today? (Espresso/Latte/Cappuccino) ''')
    if request == "report":
        print(f'''
Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g''')
        if "money" in resources:
            print("$" + str(resources["money"]))
    elif request == "off":
        exit()
    elif request == "espresso" or request == "latte" or request == "cappuccino":
        ingred = check_ingredients(request)
        if ingred == "Sufficient ingredients.":
            print("Please insert coins.")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            if "money" not in resources:
                resources["money"] = 0
            charge = charge_customer(request, quarters, dimes, nickels, pennies)
            if isinstance(charge, float):
                use_ingredients(request)
                print(f"Thank you! Here's ${charge} in change and your {request}.")
            elif isinstance(charge, str):
                print(charge)
            else:
                use_ingredients(request)
                print(f"Thank you! Here's your {request}.")
        else:
            print(ingred)
    else:
        print("Invalid request.")

MACHINE_RUNNING = True
while MACHINE_RUNNING:
    run_machine()
