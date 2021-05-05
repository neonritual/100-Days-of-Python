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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
total_money_in = 0


#TODO: 3. Check resources to complete the order
# If you don't have the resources, give apology message and RESTART


def remaining_stock_check():
    if MENU[user_order]['ingredients']['water'] < resources["water"]:
        if MENU[user_order]['ingredients']['milk'] < resources["milk"]:
            if MENU[user_order]['ingredients']['coffee'] < resources["coffee"]:
                in_stock = True
            else:
                print("sry babe")
        else:
            print("sry babe")
    else:
        print("sry babe")


#TODO: 2. Take user 'order'.
user_order = input("What would you like? (espresso / latte / cappuccino) \n")

#TODO: 1. Print 'report' of resources in a readable format.
if user_order == "report":
    for items in resources:
        print(items, resources[items])
    print(f"${total_money_in}")
elif user_order != "report":
    remaining_stock_check()


# #TODO: 4. Ask for amount of quarters, dimes, nickles, pennies.
# def insert_coins():
#     print("Please insert coins.")
#     quarters_in = int(input("How many quarters?  "))
#     dimes_in = int(input("How many dimes?  "))
#     nickels_in = int(input("How many nickels?  "))
#     pennies_in = int(input("How many pennies?  "))
#
#
#
# #TODO: 5: Calculate total of inserted money.
#
#
# def calculate_inserted_coins(quarters, dimes, nickels, pennies):
#     money_subtotal = (quarters / 4) + (dimes / 10) + (nickels / 5)
#     if pennies >= 100:
#         total_money_in = money_subtotal + pennies / 100
#     else:
#         total_money_in = money_subtotal + pennies
#     return total_money_in

#TODO: 4. Ask for amount of quarters, dimes, nickles, pennies.
def insert_coins():
    print("Please insert coins.")
    quarters_in = int(input("How many quarters?  "))
    dimes_in = int(input("How many dimes?  "))
    nickels_in = int(input("How many nickels?  "))
    pennies_in = int(input("How many pennies?  "))


    def calculate_inserted_coins(quarters, dimes, nickels, pennies):

        money_subtotal = (quarters / 4) + (dimes / 10) + (nickels / 20)
        if pennies >= 100:
            total_money_in = money_subtotal + pennies / 100
        else:
            total_money_in = money_subtotal + pennies
        return total_money_in

    return calculate_inserted_coins(quarters_in, dimes_in, nickels_in, pennies_in)

#TODO: 5: Calculate total of inserted money.

total_money_in = insert_coins()
print(f"${total_money_in}")


##TODO: 6 Determine if it is enough to buy the drink.
## If it is, calculate Change.
## If not, refund money and RESTART

#TODO: 7: Give drink and RESTART.


