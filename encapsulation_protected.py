# Protected members (in c++ or java) are those members of the class that cannot be accessed outside
# the class but can be accessed from within the class and its subclass. To accomplish this in Python,
# we use "_"

class Base:
    def __init__(self):
        self._a = 2

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of a base class: ", self._a)

        self._a = 3
        print("Calling modified protected member outside class: ", self._a)

a = Derived()
b = Base()

print("Accessing protected member of obj1: ", a._a)
print("Accessing protected member of obj2: ", b._a)