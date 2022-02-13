import pygame
from numpy import *

rami_type = array([str] * 10)
rami_pos = array([int] * 10)
a = 0
o = 0
x = 0
y = 0
z = 0
rami_cord = array([int] * 15)
rami_cord_pos = array([int] * 15)

nom = input("Saisissez le nom de l'hydrocarbure: ")
chaine_lineaire = ["méthane", "étha", "prop", "but", "pent", "hex", "hept", "oct", "non"]
ramification = ["ethyl","méthyl", "propyl"]

#toul l chaine linéaire
for i in range (9):
    test_c = nom.find(chaine_lineaire[i])
    if test_c != -1:
        type_ = chaine_lineaire[i]

#l ar9am teb3in chkoun?
for i in range(len(nom)):
    test = nom[i].isdigit()
    if test == True:
        rami_cord[o] = int(nom[i])
        rami_cord_pos[o] = i
        o = o + 1

#talaa les ramifications
for i in range (3):
    test_r = nom.find(ramification[i])
    if test_r != -1:
        rami_type[a] = ramification[i]
        rami_pos[a] = test_r
        a = a+1
if a == 1:
    rami_type_1 = array([int] * 10)
    for i in range(o):
        if rami_cord_pos[i] < rami_pos[0]:
            rami_type_1[x] = rami_cord[i]
            x = x + 1
        else:
            liaison_cord = rami_cord[i]
elif a == 2:
    rami_type_1 = array([int] * 10)
    rami_type_2 = array([int] * 10)
    for i in range(o):
        if rami_cord_pos[i] < rami_pos[0]:
            rami_type_1[x] = rami_cord[i]
            x = x + 1
        elif rami_cord_pos[i] > rami_pos[0] and rami_cord_pos[i] < rami_pos[1]:
            rami_type_2[y] = rami_cord[i]
            y = y + 1
        else:
            liaison_cord = rami_cord[i]
elif a == 3:
    rami_type_1 = array([int] * 10)
    rami_type_2 = array([int] * 10)
    rami_type_3 = array([int] * 10)
    for i in range(o):
        if rami_cord_pos[i] < rami_pos[0]:
            rami_type_1[x] = rami_cord[i]
            x = x + 1
        elif rami_cord_pos[i] > rami_pos[0] and rami_cord_pos[i] < rami_pos[1]:
            rami_type_2[y] = rami_cord[i]
            y = y + 1
        elif rami_cord_pos[i] > rami_pos[1] and rami_cord_pos[i] < rami_pos[2]:
            rami_type_3[z] = rami_cord[i]
            z = z + 1
        else:
            liaison_cord = rami_cord[i]




#alcane, alcène, wala alcyne
test_n = nom[len(nom)-3:]

if test_n == "ene" or test_n == "ène":fi = "alcène"

elif test_n == "yne": fi = "alcyne"

else: fi = "alcane"
print("Cet hydrocarbure est un", fi, "qui", end = " ")
if a ==0: print("n'admet aucune ramification")
elif a== 1:
    print("admet un seul type de ramification:", rami_type[a-1] + "e", "dans les positions", end = " ")
    for i in range (x):
        print(rami_type_1[i], ",", end = " ")
    print("et sa chaine linéaire est:", type_ + "ane", end = " ")
elif a == 2:
    print("admet deux types de ramifications:", rami_type[a-2] + "e", "et", rami_type[a-1] + "e", "respectivement dans les positions", end = " ")
    for i in range (x):
        print(rami_type_1[i], ",", end = " ")
    print("et", end = " ")
    for i in range (y):
        print(rami_type_2[i], ",", end = " ")
    print("et sa chaine linéaire est le:", type_ + "ane", end = " ")
elif a == 3:
    print("admet trois types de ramifications:", rami_type[a-3] + "e", ",", rami_type[a-2] + "e", "et", rami_type[a-1] + "e", "respectivement dans les positions", end = " ")
    for i in range (x):
        print(rami_type_1[i], ",", end = " ")
    print("et", end = " ")
    for i in range (y):
        print(rami_type_2[i], ",", end = " ")
    print("et", end = " ")
    for i in range (z):
        print(rami_type_3[i], ",", end = " ")
    print("et sa chaine linéaire est le:", type_ + "ane", end = " ")
if fi == "alcène":print(", et la position de sa double liaison est,", str(liaison_cord) + ".")
elif fi == "alcyne":print(", et la position de sa triple liaison est,", str(liaison_cord) + ".")
