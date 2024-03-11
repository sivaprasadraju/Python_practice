########################################################
            #######                     #######
            #  A  #                     #  B  #
            #######                     #######
                #                         #
                  #                     #
                    #                 #
                        #          #
                           ######
                           # C  #
                           ######
########################################################

class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)

class Father:
    fathername = ""
    def father(self):
        print(self.fathername)

class Son(Mother, Father):
    def parents(self):
        print("My Father name is {}".format(self.fathername))
        print("My Mother name is {}".format(self.mothername))

a = Son()
a.mothername = "mothername"
a.fathername = "fathername"
a.parents()