class Person(object):

         def __innit__(self,name,idnumber):
                    self.name  = name
                    self.idnumber = idnumber    

         def display(self):
                 print(self.name)
                 print(self.idnumber)


class Employee(Person):
            def __init__(self,name,idnumber,post,salary):
                    self.post = post 
                    self.salary = salary 

                    Person.__innit__(self,name,idnumber)



a = Employee("Shayan","1238764","Intern","20000")

a.display()


