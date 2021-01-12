
a_list = [1, 2, 3]
a_list_iterator = a_list.__iter__()

while True:
    try:
        an_item = a_list_iterator.__next__()
        print(an_item)
    except StopIteration:
        # because there is a StopIteration-exception eventually
        break

""" Output:

1
2
3
"""
