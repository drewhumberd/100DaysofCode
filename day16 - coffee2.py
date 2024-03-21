'''Coin-operated coffee machine, now with OOP.'''
from supportfiles.menu import Menu
from supportfiles.coffee_maker import CoffeeMaker
from supportfiles.money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

machinerunning = True

while machinerunning:
    print("What can I make for you today?")
    order = input(menu.get_items())
    if order == "off":
        machinerunning = False
    elif order == "report":
        coffeemaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(order)
        if coffeemaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)
