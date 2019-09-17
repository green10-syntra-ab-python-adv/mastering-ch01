# is_er_iets_van_waar.py
# als er iets waar is, mogen we stoppen
# voorbeeld van break

items = [0, None, 0.0, True, 0, 7]   # True en 7 zijn equivalent met True

found = False     # "vlag"

for item in items:
    print('item wordt gecheckt', item)
    if item:
        found = True   # pas vlag aan
        break

if found: # we kijken naar de vlag
    print('Op zijn minst één element is equivalent met True')
else:
    print('Alle elementen zijn False of equivalent')              
