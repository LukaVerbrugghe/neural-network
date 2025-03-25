import numpy as np
import matplotlib as plt

epoch = 1
x = 0
labelY = 0
w0 = -7
w1 = 1
learningRate = 0.1
calc = 0
groterDanNul = False
voorspellingy = 0
voorspellingGelijk = False
controlearray = [False,False,False,False,False,False]

#initiele waarde
punten = [-2,-1,2,4,5,9]
klasse = [0,0,0,1,1,1]

# functie die checkt of de eindconditie is bereikt
def epochIsGelijk():
    for i in range(len(controlearray)):
        if controlearray[i] == False:
            return False
            break
    return True



def doorloopEenEpoch(epoch):
    print("")
    # print de huidige epoch
    print("Epoch " + str(epoch))
    # we moeten voor een epoch alle 6 de punten doorlopen
    for i in range(len(punten)):
        x = punten[i]
        labelY = klasse[i]
        calc = w1 * x + w0
        if calc < 0:
            groterDanNul = False
            voorspellingy = 0
        else:
            groterDanNul = True
            voorspellingy = 1

        if voorspellingy == labelY:
            voorspellingGelijk = True
            controlearray[i] = True
        else:
            voorspellingGelijk = False
            controlearray[i] = False
        # print het punt
        print("P" + str(i + 1))
        print("X = " + str(x))
        print("Label y = " + str(labelY))
        print("w1 * x + w0 = " + str(w1) + " * " + str(x) + " + " + str(w0) + " = " + str(calc))
        print("Groter dan 0: " + str(groterDanNul))
        print("Voorspelling y hoedje = " + str(voorspellingy))
        print("Voorspelling gelijk aan effectieve waarde: " + str(voorspellingGelijk))
        print("")
        print("")

def aanpassenWeight0():
    return w0 + learningRate * ()

def aanpassenWeight1():
    return 0

while not epochIsGelijk():
    doorloopEenEpoch()
    epoch+=1
    if epochIsGelijk():
        print("Het neuraal netwerk is getraind met volgende waarden")
        print("W0 = " + str(w0))
        print("W1 = " + str(w1))
        print("Epoch = " + str(epoch - 1))
    else:
        print("De waarden zijn nog niet correct")
        print("Huidige waarden")
        print("W0 = " + str(w0))
        print("W1 = " + str(w1))
        print("Epoch = " + str(epoch - 1))
        print("")
        print("De waarden zijn nog niet correct en worden aangepast")
        w0 = aanpassenWeight0()
        w1 = aanpassenWeight1()