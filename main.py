# # import another_module
# # print(another_module.another_variable)
#
# # import turtle
# # timmy = turtle.Turtle()
# import turtle
# from turtle import Turtle, Screen
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkViolet")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l" # используем атрибут   https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
#set_style()


print(table)

