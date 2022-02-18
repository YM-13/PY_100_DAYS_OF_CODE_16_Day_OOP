from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine
coffee_money = MoneyMachine()
process_coffee = CoffeeMaker()
drinks_order = Menu()
drink_menu = drinks_order.get_items()

machine_is_on = True
while machine_is_on:
	order_name = input(f"What would you like ({drink_menu})?: ")

	"""Получаем объект со всеми данными по напитку"""


	if order_name == "report":
		process_coffee.report()
		coffee_money.report()
	elif order_name == "off":
		machine_is_on = False
	else:
		menu_item_object = drinks_order.find_drink(order_name)
		if process_coffee.is_resource_sufficient(menu_item_object) and coffee_money.make_payment(menu_item_object.cost):
			# price = menu_item_object.cost  Получает цену из объекта !!!!!!!
			process_coffee.make_coffee(menu_item_object)

