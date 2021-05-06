from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


print("Welcome to the coffee maker!")
todays_menu = Menu()
todays_coffeemaker = CoffeeMaker()
todays_moneymachine = MoneyMachine()

power_on = True


while power_on:
    menu_items = todays_menu.get_items()
    user_order = input(f"What would you like? {menu_items}")
    if user_order == "off":
        power_on = False
    elif user_order == "report":
        todays_coffeemaker.report()
        # todays_moneymachine.report()
    else:
        user_drink = todays_menu.find_drink(user_order)
        if todays_coffeemaker.is_resource_sufficient(user_drink) and todays_moneymachine.make_payment(user_drink.cost):
            todays_coffeemaker.make_coffee(user_drink)





#TODO: 2. Take user Order.
#   TODO: 1. Print 'report' of resources in a readable format.
#TODO: 3. Check resources to complete order.
# if todays_coffeemaker.is_resource_sufficient(todays_menu.find_drink(user_order)):
#     print("Thank you for your order.")
#TODO: 4. Ask for amount in quarters, dimes, nickels, pennies.
#TODO: 5. Calculate total of inserted money.
#TODO: 6. Determine if t is enough to buy the drink.
#TODO: 7. Calculate Change of money sufficient.
# TODO: 8. Give drink.
#TODO: 9. RESTART.




