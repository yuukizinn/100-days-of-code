from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    order = input(f"please select {menu.get_items()}\n")
    if order == "off":
        exit()
    elif order == "resource":
        print(coffee_maker.resources)
    elif order == "report":
        money_machine.report()
    elif order == "latte" or order == "espresso" or order == "cappuccino":
        choice = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(choice):
            money_machine.make_payment(choice.cost)
            coffee_maker.make_coffee(choice)
    else:
        print("wrong words")

