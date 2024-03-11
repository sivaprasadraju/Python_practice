######################################################
                  #########
                  #       # Parent class
                  #########
                      #
                      #
                  #########
                  #       # Child class
                  #########
######################################################

class Parent:
    def func1(self):
        print("This function is in parent class")

class Child(Parent):
    def func2(self):
        print("This function is in child class")

a = Child()
a.func1()
a.func2()