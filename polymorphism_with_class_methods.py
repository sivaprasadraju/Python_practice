class India():
    def capital(self):
        print("New Delhi is the capital of Inida")
    def language(self):
        print("Hindi is the most widely spoken language in India")
    def type(self):
        print("India is developed country")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA")
    def language(self):
        print("English is the primary language of USA")
    def type(self):
        print("USA is developed country")

def func(obj):
    obj.capital()
    obj.language()
    obj.type()

obj_ind = India()
obj_usa = USA()

# Polymorphism using function
# func(obj_ind)
# func(obj_usa)

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()