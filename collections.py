# Definición de una lista
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

# Acceso a una lista por posición
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

# Modificación de los valores de una lista
myFruitList[2] = "orange"
print(myFruitList)
myFruitList.append("lemon")
print(myFruitList)
myFruitList.remove("orange")
print(myFruitList)

# Definición de una tupla
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

# Acceso a una tupla por posición
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

# Definición de un diccionario
myFavoriteFruitDictionary = {
    "Akua":"apple",
    "Saanvi":"banana",
    "Paulo":"pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

# Acceso al diccionario por nombre
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
