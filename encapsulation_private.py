# Private members are similar to protected members, the difference is that the class members declared
# private should neither be accessed outside the class not by any base class.
# In python, there is no existence of Private instance variables that cannot be accessed except inside a class
# to define private member, we use "__" double underscore

class Base:
    def __init__(self):
        self.a = "Public member"
        self.__c = "Private member"

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)

a = Base()
print(a.a)
