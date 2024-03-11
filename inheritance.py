class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("My ID number is {}".format(self.idnumber))

class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary= salary
        self.post = post

        Person.__init__(self, name, idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("My ID number is {}".format(self.idnumber))
        print("Post: {}".format(self.post))

a = Employee("Rahul", 1234, 20000, "Intern")

a.display()
a.details()