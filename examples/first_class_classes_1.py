import types

def func1(obj):
    print("I am func1 and I am called from obj", obj)

def func2(obj):
    print("I am func2 and I am called from obj", obj)

class A:
    def func_z(self):
        print("I am func_z and I am called from obj", self)

a = A()
A.func_y = func2
a.func_x = types.MethodType(func1,a)

a.func_z()
a.func_y()
a.func_x()





