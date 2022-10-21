from concurrent.futures import process
import os
clear = lambda: os.system('cls')

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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def isResourceSufficient(ingredients):
    for item in ingredients:
        if(ingredients[item] >= resources[item]):
            print(f"Sorry there is not enough {item}")
            return False
        return True


def processCoins():
    print("Please insert coins.")
    total = 0
    total += int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def isTransactionSuccessful(payment, drink_cost):
    if(payment >= drink_cost):
        change = round(payment - drink_cost, 2)
        print(f"Here is the change. {change}")
        global profit
        profit += round(payment - change, 2)
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def makeCoffe(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]

    print(f"And here's your {drink_name}")

def coffeeMachine():
    clear()
    is_on = True
    while is_on == True:
        choice = input("What would you like to have? (espresso/latte/cappuccino: ")
        if(choice == 'report'):
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}") 
        elif(choice == 'off'):
            is_on = False
        else:
            drink = MENU[choice]
            if(isResourceSufficient(drink['ingredients'])):
                payment = processCoins()
                if isTransactionSuccessful(payment, drink["cost"]):
                    makeCoffe(choice,drink["ingredients"])


coffeeMachine()
            

            