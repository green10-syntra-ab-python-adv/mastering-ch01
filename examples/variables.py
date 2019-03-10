# module variables.py

import inspect

# LEGB Local, Enclosing, Global, Builtin

this_function_name = inspect.currentframe().f_code.co_name
var1 = "Global from {}".format(this_function_name)

def enclosing_function():
    this_function_name = inspect.currentframe().f_code.co_name
    var2 = "Enclosing from {}".format(this_function_name)

    def inner_function():
        this_function_name = inspect.currentframe().f_code.co_name
        var3 = "Inner from {}".format(this_function_name)
        print ("Inner: ", var1, var2, var3)

    # var3 is not known here
    print ("Enclosing: ", var1, var2)
    inner_function()


# var2 and var3 are not known here
print ("Outer: ", var1)
enclosing_function()
