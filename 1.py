# CTRL + K / C
# CTRL + K / U

#a = 1
#[print(i) for i in range(10)]

# for i in range (10):
#     a+=1
#     print(a)

# elements = ["a","b","c"]

# for element in elements:
#     print("Ma lettre : {}".format(element))

# a = ["a","b","c"]
# b = 1

# for number,i in enumerate(a) :
#     print(f"{number}. Ma lettre : {i} ")

# def maFonction():
#     print("Hello World")
#     return "mon retour"

# print(maFonction)

# def mafonction(texte, nombre):
#     return texte * nombre
# print(mafonction("Hello World   ", 5))

import os
import sys

liste = os.listdir("C:\\Users")

for nb,i in enumerate(liste):
    print(f"{nb}. {i}")
print(liste)

print (sys.argv[0])


import os
import sys

path = (sys.argv[1])

liste = (os.listdir(path))

for nb,i in enumerate(liste):
    print (f"{nb}. {i}")
print(liste)