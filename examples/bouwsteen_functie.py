import math

def voorbeeld_functie(naam, straal):
    oppervlakte = math.pi * straal ** 2
    return "De oppervlakte van {} is {}".format(naam, oppervlakte)

print(voorbeeld_functie('een mooie cirkel', 10))