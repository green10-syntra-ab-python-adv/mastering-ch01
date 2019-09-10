expression1 = True
expression2 = False
expression3 = False

def do_a():
    pass

def do_b():
    pass

do_f = do_e = do_d = do_c = do_a

iterable = [1, 2, 3]


if expression1:
    do_a()
    do_b()
elif expression2:
    do_c()
    do_d()
else:
    do_e()
    do_f()

while expression3:
    do_a()
    do_b()

for x in iterable:
    do_c()
    do_d()
    do_e()

d = dict()
d['voornaam'] = 'Hans'
d['familienaam'] = 'Vandenbogaerde'
d['stad'] = "Mechelen"

for key, value in d.items():
    print(key + " is " + value)

"""Result is

voornaam is Hans
familienaam is Vandenbogaerde
stad is Mechelen
"""

# Comprehension

this_list = [2*x for x in range(9)]
print(this_list)

# Prints [0, 2, 4, 6, 8, 10, 12, 14, 16]

first_names = ["Peter", "Petra", "Pieter"]
last_names = ["De Roover", "De Sutter", "De Crem"]

for index, (first_name, last_name) \
        in enumerate(zip(first_names, last_names)):

    print(index+1, first_name, last_name)

"""Yields:

1 Peter De Roover
2 Petra De Sutter
3 Pieter De Crem
"""
