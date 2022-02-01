"""
Het programma belastingvrije_som_2_match_case.py berekent de belastingvrije som
Het past daarbij het nieuwe match case statement toe

De parameter die wordt meegegeven is het aantal kinderen ten laste
Indien er geen parameter wordt meegegeven, is het aantal kinderen ten laste O
"""
import sys

# Ook het volgende is een compactere schrijfwijze
aantal_kinderen = int(sys.argv[1]) if len(sys.argv) >=2 else 0

print("Aantal kinderen: ", aantal_kinderen)

belastingvrije_som = 9050.00

match aantal_kinderen:
    case 0: belastingvrije_som += 0.00
    case 1: belastingvrije_som += 1650.00
    case 2: belastingvrije_som += 4240.00
    case 3: belastingvrije_som += 9500.00
    case 4: belastingvrije_som += 15360.00
    case _: belastingvrije_som += 15360.00 + (aantal_kinderen - 4) * 5860.00

print("Belastingvrije som: ", belastingvrije_som)



