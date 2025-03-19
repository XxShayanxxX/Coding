class student :
    grade = 8 
    name = "shayan"

    def introduction(self):
        print("Hi i am shayan")
    
    def detailed(self):
        print("hi i am ", self.name)
        print("I am from grade", self.grade)
    

object = student()
object.introduction()
object.detailed()
