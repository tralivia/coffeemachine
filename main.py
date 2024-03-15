from Menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from MoneyMachine import MoneyMachine
is_on = True
menu = Menu
menuitems = MenuItem
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
while is_on:
    options = menu.get_items()
    choice = input(f"what would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        MoneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
           if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)