from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine
coffee_money = MoneyMachine()
process_coffee = CoffeeMaker()
drinks_order = Menu()

order_name = input(f"What would you like ({drinks_order.get_items()})?: ")
menu_item_object = drinks_order.find_drink(order_name)
"""Получаем объект со всеми данными по напитку"""
if order_name == "report":
	process_coffee.report()
	coffee_money.report()


else:
	if process_coffee.is_resource_sufficient(drinks_order.find_drink(order_name)) != None:
		#coffee_money.make_payment(MenuItem(drinks_order.find_drink(order_name)))
		print(drinks_order.find_drink(order_name))
		process_coffee.make_coffee(drinks_order.find_drink(order_name))
	else:
		print("Impossible to make")






