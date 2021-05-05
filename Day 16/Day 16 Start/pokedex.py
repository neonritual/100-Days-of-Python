#################################
#### Practice using Packages ####
#################################

## First went to PyPi.org and found PrettyTable, then searched from PyCharm -->
# Preferences --> Python Interpreter ---> The + and search to add it.

from prettytable import PrettyTable
table = PrettyTable()
table.header = True
table.header_style = "upper"
table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Bulbasaur", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Grass", "Water"])

print(table)