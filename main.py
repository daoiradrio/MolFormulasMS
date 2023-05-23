import periodictable as pse
import math
import itertools


# TO DO:
# - objektorientiert!
# - mehr/bessere Kriterien um sinnlose Summenformeln ausschließen zu können
# - umschreiben, sodass Komplexität mit höherer Masse & weiteren isotopischen Elementen nicht so stark anwächst
#   (Berechnungsdauer steigt merklich)
#   --> was hat größeren Einfluss: Hohe Masse oder hohe Anzahl an isotopischen Elementen?
# - wie berücksichtigt man Silicium korrekt in der Doppelbindungsäquivalente?? einfach nur 2*Si?
# - wie Berechnung der DBE wenn kein Kohlenstoff, sondern z.B. nur Stickstoff, Bor oder Chlor und Wasserstoff
#   enthalten (beachten, dass Verbindungen wie Stickstoffsäure HN3 immernoch korrekt werden)?


indices_ges = {0 : "Cl", 1 : "Br", 2 : "S", 3 : "Si", 4 : "B", 5 : "C", 6 : "H", 7 : "N", 8 : "P", 9 : "O",
               10 : "F", 11 : "I"}

masses = {"C" : pse.carbon.mass, "H" : pse.hydrogen.mass, "N" : pse.nitrogen.mass, "O" : pse.oxygen.mass,
          "F" : pse.fluorine.mass, "Cl" : pse.chlorine.mass, "Br" : pse.bromine.mass, "I" : pse.iodine.mass,
          "Si" : pse.silicon.mass, "P" : pse.phosphorus.mass, "S" : pse.sulfur.mass, "B" : pse.boron.mass}

isotopic = {0 : "Cl", 1 : "Br", 2 : "S", 3 : "Si", 4 : "B"}

translate = {"J" : True, "N" : False}


def calc_mass(liste):
    mass = 0
    for item in liste:
        mass += masses.get(item)
    return mass


def calc_dbe(liste):
    C = liste.count("C")
    Si = liste.count(("Si"))
    return ((2*C + 2)*(C != 0) + (2*Si*(Si != 0)) - liste.count("H") + liste.count("N") + liste.count("B") \
             + liste.count("P") - liste.count("F") - liste.count("Cl") - liste.count("Br") - liste.count("I"))/2


def print_formulas(liste):
    for formula in liste:
        element_list = [[], [], [], [], [], [], [], [], [], [], [], []]
        result = ""
        for element in formula:
            if element == "C":
                element_list[0].append(element)
            elif element == "H":
                element_list[1].append(element)
            elif element == "Si":
                element_list[2].append(element)
            elif element == "N":
                element_list[3].append(element)
            elif element == "P":
                element_list[4].append(element)
            elif element == "F":
                element_list[5].append(element)
            elif element == "Cl":
                element_list[6].append(element)
            elif element == "Br":
                element_list[7].append(element)
            elif element == "I":
                element_list[8].append(element)
            elif element == "O":
                element_list[9].append(element)
            elif element == "S":
                element_list[10].append(element)
            elif element == "B":
                element_list[11].append(element)

        for element in element_list:
            if len(element) == 1:
                result += element[0]
            elif len(element) == 0:
                pass
            else:
                result += element[0] + str(len(element))

        print()
        print("SUMMENFORMEL: " + result)
        print("MASSE: {:.5f}".format(calc_mass(formula)))
        print("DBE: {}".format(int(calc_dbe(formula))))


def try_combinations(elements, mass, error):
    formulas = []
    for a,b,c,d,e,f,g,h,i,j,k in itertools.product(elements[0], elements[1], elements[2], elements[3], \
                                                   elements[4], elements[5], elements[7], elements[8], \
                                                   elements[9], elements[10], elements[11]):
        formula = []
        for x1 in range(a):
            formula.append(indices_ges.get(0))
        for x2 in range(b):
            formula.append(indices_ges.get(1))
        for x3 in range(c):
            formula.append(indices_ges.get(2))
        for x4 in range(d):
            formula.append(indices_ges.get(3))
        for x5 in range(e):
            formula.append(indices_ges.get(4))
        for x6 in range(f):
            formula.append(indices_ges.get(5))
        for x7 in range(g):
            formula.append(indices_ges.get(7))
        for x8 in range(h):
            formula.append(indices_ges.get(8))
        for x9 in range(i):
            formula.append(indices_ges.get(9))
        for x10 in range(j):
            formula.append(indices_ges.get(10))
        for x11 in range(k):
            formula.append(indices_ges.get(11))

        if formula:
            pass
        else:
            continue

        formula_mass = calc_mass(formula)
        if (mass + error) < formula_mass:
            continue
        else:
            pass

        while mass > formula_mass:
            formula.append("H")
            formula_mass = calc_mass(formula)
            if (mass - error) < formula_mass < (mass + error):
                break

        formula_mass = calc_mass(formula)
        dbe = calc_dbe(formula)
        if (mass - error) < formula_mass < (mass + error) and dbe >= 0 and (dbe % 1) == 0:
            formulas.append(formula)

    return formulas


# ZUM TESTEN:
print(8*pse.sulfur.mass)
# ANSONSTEN LÖSCHEN
elements = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
formulas = []
mass = float(input("Exakte Masse: "))
error = float(input("Fehler: "))
if int(mass) % 2 == 0:
    for i in range(1, math.ceil(mass/pse.carbon.mass)):
        elements[5].append(i)
    for j in range(1, math.ceil(mass/pse.oxygen.mass)):
        elements[9].append(j)
    for k in range(1, math.ceil(mass/pse.fluorine.mass)):
        elements[10].append(k)
    for l in range(1, math.ceil(mass/pse.iodine.mass)):
        elements[11].append(l)
    for m in range(2, math.ceil(mass/pse.nitrogen.mass), 2):
        elements[7].append(m)
    for n in range(1, math.ceil(mass/pse.phosphorus.mass)):
        elements[8].append(n)

    if translate.get(input("Isotopenmuster (J/N)?: ")):
        for element in isotopic:
            if translate.get(input("{} (J/N)?: ".format(isotopic.get(element)))):
                for i in range(1, math.ceil(mass/masses.get(isotopic.get(element)))):
                    elements[element].append(i)

    formulas = try_combinations(elements, mass, error)

else:
    for i in range(1, math.ceil(mass/pse.carbon.mass)):
        elements[5].append(i)
    for j in range(1, math.ceil(mass/pse.oxygen.mass)):
        elements[9].append(j)
    for k in range(1, math.ceil(mass/pse.fluorine.mass)):
        elements[10].append(k)
    for l in range(1, math.ceil(mass/pse.iodine.mass)):
        elements[11].append(l)
    for m in range(1, math.ceil(mass/pse.nitrogen.mass), 2):
        elements[7].append(m)
    for n in range(1, math.ceil(mass/pse.phosphorus.mass)):
        elements[8].append(n)

    if translate.get(input("Isotopenmuster (J/N)?: ")):
        for element in isotopic:
            if translate.get(input("{} (J/N)?: ".format(isotopic.get(element)))):
                for i in range(1, math.ceil(mass/masses.get(isotopic.get(element)))):
                    elements[element].append(i)

    formulas = try_combinations(elements, mass, error)

print_formulas(formulas)
