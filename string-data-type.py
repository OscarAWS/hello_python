# Se denomina script a un archivo de texto que contiene una secuencia lógica de comandos.
myString = "This is a string."
print(myString)

# Presentar el tipo de dato de cadena
print(type(myString))

# Caracteres de escape
print("\"" + myString + "\"" + " is of the data type " + str(type(myString)) + "\n")

# Trabajar con concatenación de cadenas
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

# Trabajar con cadenas de entrada
name = input("What is your name? ")
print(name)

# Dar formato a las cadenas de salida
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))

