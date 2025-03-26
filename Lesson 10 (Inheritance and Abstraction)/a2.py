class Parent:
    def __init__(self,firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)

class Child(Parent):
    def __init__(self,firstname,lastname,year):
        super().__init__(firstname,lastname)
        self.year = year

    
x = Child("James", "Bond" ,"1973")
x.printname()

print(x.year)


