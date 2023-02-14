from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while True:


    drink = input("What would you like? " + menu.get_items() + " ")

    if drink == "report":
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(drink) != None:
        drink = menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)




