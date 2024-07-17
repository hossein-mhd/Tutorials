# import MyModule

# MyModule.greeting("hossein")

# car = MyModule.cars["benz"]
# print(car)

##################################################

# Naming a Module
# You can name the module file whatever you like, but it must have the file extension .py
# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword

# import MyModule as MM

# MM.greeting("hossein")

# car = MM.cars["bmw"]
# print(car)

##################################################

# import platform

# OS = platform.system()
# print(OS)

##################################################

# Import From Module

from MyModule import cars

print(cars["haima"])

#  When importing using the from keyword, do not use the module name when referring to elements in the module.
#  Example: person1["age"], not mymodule.person1["age"]