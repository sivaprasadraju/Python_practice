#################################################################
                            #########
                            #       # Base Class
                            #########
                                #
                                #
                            #########
                            #       # Intermediate Class
                            #########
                                #
                                #
                            #########
                            #       # Derived Class
                            #########
##################################################################


class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername

        Grandfather.__init__(self, grandfathername)
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)
    def print_names(self):
        print("Grandfather name is {}".format(self.grandfathername))
        print("Father name is {}".format(self.fathername))
        print("Son name is {}".format(self.sonname))

a = Son( "sonname", "fathername", "grandfathername")
print(a.grandfathername)
a.print_names()