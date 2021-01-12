"""
Het programma belastingvrije_som_2_switcher.py berekent de belastingvrije som
Het past daarbij het Python-alternatief voor switch-case dictionary mapping toe

De parameter die wordt meegegeven is het aantal kinderen ten laste
Indien er geen parameter wordt meegegeven, is het aantal kinderen ten laste O
"""
import sys

if ( len(sys.argv) == 1 ):
    aantal_kinderen = 0
else:
    aantal_kinderen = int(sys.argv[1])

print("Aantal kinderen: ", aantal_kinderen)

belastingvrije_som = 9050.00

# een "lambda" is een anonieme functie

switcher = {
    0: lambda: 0.00,
    1: lambda: 1650.00,
    2: lambda: 4240.00,
    3: lambda: 9500.00,
    4: lambda: 15360.00
}
# het tweede argument van get is de default keuze
# de \ is een teken om de code over meerdere lijnen te kunnen splitsen
# de "()" op het einde zorgt voor het uitvoeren van de gekozen lambda

belastingvrije_som += \
    switcher.get(aantal_kinderen, lambda: 15360.00 + (aantal_kinderen - 4) * 5860.00)()

print("Belastingvrije som: ", belastingvrije_som)



