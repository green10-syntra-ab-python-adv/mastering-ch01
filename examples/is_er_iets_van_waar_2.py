# is_er_iets_van_waar_2.py
# Als er iets waar is, mogen we stoppen
# Voorbeeld van break en else op loop

items = [ 0, None, 0.0, "", 7, [] ]   # Alles is False

for item in items:
    print('item wordt gecheckt', item)
    if item:
        print('Op zijn minst één element is equivalent met True')
        break

# dankzij else op for hebben we geen vlag nodig
# else wordt uitgevoerd als break niet gebruikt wordt

else:
    print('Alle elementen zijn False of equivalent')              
