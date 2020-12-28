# Het programma belastingvrije_som_2_switcher.py berekent de belastingvrije som
# Het past daarbij het Python-alternatief voor switch-case dictionary mapping toe

# De eerste parameter die wordt meegegeven is het aantal kinderen ten laste
# Indien er geen parameter wordt meegegeven, is het aantal kinderen ten laste O

# De 2de parameter die wordt meegegeven is het aantal kinderen jonger dan 3 jaar
# waarvoor geen kinderopvang wordt afgetrokken
# Indien er geen 2de parameter wordt meegegeven, is dit aantal kinderen O

import sys

if ( len(sys.argv) == 1 ):
    aantal_kinderen = 0
    aantal_jonger_dan_3 = 0
elif ( len(sys.argv) == 2 ):
    aantal_kinderen = int(sys.argv[1])
    aantal_jonger_dan_3 = 0
else:
    aantal_kinderen = int(sys.argv[1])
    aantal_jonger_dan_3 = int(sys.argv[2])

if (aantal_jonger_dan_3 <= aantal_kinderen):

    print("Aantal kinderen: ", aantal_kinderen)
    print("Aantal jonger dan 3 jaar: ", aantal_jonger_dan_3)

    belastingvrije_som = 7090.00

    # een "lambda" is een anonieme functie

    switcher = {
        0: lambda: 0.00,
        1: lambda: 1510.00,
        2: lambda: 3880.00,
        3: lambda: 8700.00,
        4: lambda: 14060.00
    }
    # het tweede argument van get is de default keuze
    # de \ is een teken om de code over meerdere lijnen te kunnen splitsen
    # de "()" op het einde zorgt voor het uitvoeren van de gekozen lambda

    belastingvrije_som += \
        switcher.get(aantal_kinderen, lambda: 14060.00 + (aantal_kinderen - 4) * 5370.00)()

    belastingvrije_som += 560.00 * aantal_jonger_dan_3

    print("Belastingvrije som: ", belastingvrije_som)

else:
    print("De ingevoerde parameters zijn niet correct")
    


