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


def check_resources(drink):
    menu_ingredients = MENU[drink]['ingredients']
    for ingredient in menu_ingredients:
        if resources[ingredient] < menu_ingredients[ingredient]:
            print(f'Sorry there is not enough {ingredient}')
        else:
            return print("Please insert coins")


def check_amount(menu, selected_drink):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    inserted_money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    if inserted_money < menu[selected_drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        if "money" in resources:
            resources["money"] += menu[selected_drink]["cost"]
        else:
            resources["money"] = menu[selected_drink]["cost"]
        change = inserted_money - menu[selected_drink]["cost"]
        if not change == 0:
            print(f"Here is ${change:.2f} in change.")
        for value in menu[selected_drink]["ingredients"]:
            resources[value] -= menu[selected_drink]["ingredients"][value]
        print(f"Here is your {selected_drink}. Enjoy!")


off = False
while not off:
    selection = input("What would you like? (espresso/latte/cappuccino): ")
    if selection == "report":
        for item in resources:
            if item == "water" or item == "milk":
                print(f"{item.title()}: {resources[item]}ml")
            elif item == "coffee":
                print(f"{item.title()}: {resources[item]}g")
            else:
                print(f"{item.title()}: ${resources[item]}")
    elif selection == "off":
        off = True
    elif selection == "espresso" or selection == "latte" or selection == "cappuccino":
        check_resources(selection)
        check_amount(MENU, selection)
    else:
        print("Please type in a valid drink (espresso/latte/cappuccino)")
