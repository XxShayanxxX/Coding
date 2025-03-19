class robot:
    def __innit__(self, name , color , weight):
        self.name = name
        self.color = color 
        self.weight = weight


    def introduce_self(self):   
        print("My name is " + self.name)
        print("My color is " + self.color)
        print("My weight is " + self.weight)

r1 =  robot("Bell", "Black", 100)
r2 =  robot("james", "white", 200)
r1.introduce_self()
r2.introduce_self()

