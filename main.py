from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True
while machine_on:
    order = input(f"  What would you like? ({menu.get_items()}): ").lower()
    if order == 'off':
        machine_on = False
    elif order == 'report':
        coffee_maker.report()
    else:
        drink_order = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink_order):
            if money_machine.make_payment(drink_order.cost):
                coffee_maker.make_coffee(drink_order)
            else:
                machine_on = False
