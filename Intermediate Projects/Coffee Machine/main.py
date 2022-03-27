import os
import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 1000,
    "milk": 1000,
    "coffee": 500,
    "money": 0,
}


def clearconsole():
    """Clears the console as you play the game"""
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def resource_report():
    """prints report of water, milk, coffee, and money being held in the coffee machine"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = "{:.2f}".format((float(resources["money"])))
    print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: ${money}")


def resource_sufficient(order):
    """checks if user's order request can be made based on resources currently in the machine"""
    water_request = int(MENU[order]["ingredients"]["water"])
    milk_request = int(MENU[order]["ingredients"]["milk"])
    coffee_request = int(MENU[order]["ingredients"]["coffee"])
    if water_request > resources["water"] or milk_request > resources["milk"] or coffee_request > resources["coffee"]:
        return False
    else:
        return True


def money_enough(product, quarters, dimes, nickels, pennies):
    """Calculates if user has enough money for the product chosen, and if so,
    reduces resources by the materials needed to create product. Adds and tracks
    money being stored in the machine from purchase. Prints change given to user."""
    product_cost = (MENU[user_request]["cost"])
    user_paid = quarters + dimes + nickels + pennies
    change = format((user_paid - product_cost), ".2f")
    if user_paid >= product_cost:
        resources["water"] = int(resources["water"]) - int(MENU[user_request]["ingredients"]["water"])
        resources["milk"] = int(resources["milk"]) - int(MENU[user_request]["ingredients"]["milk"])
        resources["coffee"] = int(resources["coffee"]) - int(MENU[user_request]["ingredients"]["coffee"])
        resources["money"] = float(resources["money"]) + (float(product_cost))
        print(f"Here is ${change} in change.\nHere is your {user_request}, enjoy!\n")
        if input("Do you want to place another order? Type 'y' or 'n': ").lower() == 'y':
            clearconsole()
        else:
            print("Thank you for your order, next customer please.")
            time.sleep(3)
            clearconsole()

    else:
        print("\nSorry that's not enough money. Money refunded.")
        if input("Do you want to place another order? Type 'y' or 'n': ").lower() == 'y':
            clearconsole()
        else:
            print("Thank you for your order, next customer please.")
            time.sleep(3)
            clearconsole()


# main program
machine_on = True
while machine_on:
    print("You can order an espresso, latte, or cappuccino.")
    user_request = input("What would you like?: ").lower()
    if user_request == "off":
        machine_on = False
        
    while user_request == "report":
        resource_report()
        user_request = input("\nWhat would you like?: ").lower()

    if resource_sufficient(user_request) == True:
        print("Please insert coins.\n")
        quarters_sum = (int(input("How many quarters?: "))) * .25
        dimes_sum = (int(input("How many dimes?: "))) * .10
        nickels_sum = (int(input("How many nickels?: "))) * .05
        pennies_sum = (int(input("How many pennies?: "))) * .01

        money_enough(user_request, quarters_sum, dimes_sum, nickels_sum, pennies_sum)
    else:
        print("Sorry, the machine is running low on ingredients.")
