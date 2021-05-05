from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_in_till = 0
user_money = 0


#TODO: 2. Take user Order.
#   TODO: 1. Print 'report' of resources in a readable format.

print("Welcome to the coffee maker!")
todays_menu = Menu()
todays_coffeemaker = CoffeeMaker()
todays_moneymachine = MoneyMachine()

user_order = input(f"What would you like? {todays_menu.get_items()}")
if todays_menu.find_drink(user_order) != None:
    None
elif user_order == "report":
    print(todays_coffemaker.report())


#TODO: 3. Check resources to complete order.
if todays_coffeemaker.is_resource_sufficient(todays_menu.find_drink(user_order)):
    print("YAY all set")
#TODO# IF you don't have the resources, say sorry and RESTART.


#TODO: 4. Ask for amount in quarters, dimes, nickels, pennies.

#TODO: 5. Calculate total of inserted money.
#TODO: 6. Determine if t is enough to buy the drink.
#TODO: 7. Calculate Change of money sufficient.
#TODO: 8. Give drink.
#TODO: 9. RESTART.




