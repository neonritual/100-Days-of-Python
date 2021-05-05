from art import logo

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

print(logo)


def start_coffee_maker():
    total_money_in = 0
    money_in_till = 0


    #TODO: 3. Check resources to complete the order
    # If you don't have the resources, give apology message and RESTART


    def remaining_stock_check():
        if MENU[user_order]['ingredients']['water'] < resources["water"]:
            if MENU[user_order]['ingredients']['milk'] < resources["milk"]:
                if MENU[user_order]['ingredients']['coffee'] < resources["coffee"]:
                    resources["water"] -= MENU[user_order]['ingredients']['water']
                    resources["milk"] -= MENU[user_order]['ingredients']['milk']
                    resources["coffee"] -= MENU[user_order]['ingredients']['coffee']
                    print(resources)
                else:
                    print("Sorry, we are out of stock.")
                    start_coffee_maker()
            else:
                print("Sorry, we are out of stock.")
                start_coffee_maker()
        else:
            print("sSorry, we are out of stock.")
            start_coffee_maker()

    #TODO: 2. Take user 'order'.
    user_order = input("What would you like? (espresso / latte / cappuccino) \n")
    if user_order not in MENU:
        print("Sorry, I didn't quite get that.")
        start_coffee_maker()

    #TODO: 1. Print 'report' of resources in a readable format.
    if user_order == "report":
        for items in resources:
            print(items, resources[items])
        print(f"${money_in_till}")
    elif user_order != "report":
        remaining_stock_check()


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
    #TODO: 7: Give drink
    if total_money_in > MENU[user_order]["cost"]:
        user_change = total_money_in - MENU[user_order]["cost"]
        print(f"Here is {user_change} in change.")
        print("Here is your drink!")
        money_in_till += total_money_in - user_change

    else:
        print("Sorry, that's not enough.")
    # TODO: 8 RESTART
    start_coffee_maker()

start_coffee_maker()






