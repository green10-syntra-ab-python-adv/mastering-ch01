def foo():
    print("I'm a lovely foo()-function")

print(foo)
# <function foo at 0x7f9b75de3f28>

print(foo.__class__)
# <class 'function'>

bar = foo
bar()
# I'm a lovely foo()-function
print(bar.__name__)
# foo

def do_something(what):
    """Executes a function

    :param what: name of the function to be executed
    """
    what()

do_something(foo)
# I'm a lovely foo()-function

def try_me(self):
    print('I am '+self.name)
    print("I was created by " + self.creator)
    print("This is wat I do")
    self()

# a function is an object with attributes and methods
setattr(foo, 'name', 'foo')
foo.creator = "Hans"
foo.print = try_me
foo.print(foo)
"""
I am foo
I was created by Hans
This is wat I do
I'm a lovely foo()-function
"""

print(foo)
# <function foo at 0x7f9b75de3f28>


