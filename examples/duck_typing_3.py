import abc

class Bird(abc.ABC):
    @abc.abstractmethod
    def fly(self):
        pass

class Duck(Bird):
    def fly(self):
        print("Duck flying")

class Eagle(Bird):
    def fly(self):
        print("Eagle flying")
    def dive(self):
        print("Eagle diving")

class Airplane:
    def fly(self):
        print("Airplane flying")

class Whale:
    def swim(self):
        print("Whale swimming")

def lift_off(entity):
    try:
        entity.fly()
    except:
        print("The object is from class {}, that does not have a fly method"
                    .format(entity.__class__))


duck = Duck()
airplane = Airplane()
whale = Whale()
eagle = Eagle()

print(issubclass(Duck, Bird))
print(issubclass(Airplane, Bird))
print(issubclass(Whale, Bird))
print(issubclass(Eagle, Bird))

lift_off(duck) # prints `Duck flying`
lift_off(airplane) # prints `Airplane flying`
lift_off(whale) # Throws the error `'Whale' object has no attribute 'fly'`
lift_off(eagle)