##########################################################################
                                #######
                                #  A  #
                                #######
                                   #
                                   #
                ########################################
                #                   #                  #
                #                   #                  #
            #########           #########           #######
            #   B   #           #   C   #           #  D  #
            #########           #########           #######

###########################################################################

class Parent:
    def func1(self):
        print("This function is in parent class")

class Child1(Parent):
    def func2(self):
        print("This function is in child1 class")

class Child2(Parent):
    def func3(self):
        print("This function is in child2 class")

a = Child2()
b = Child1()
a.func1()
a.func3()
b.func1()
b.func2()