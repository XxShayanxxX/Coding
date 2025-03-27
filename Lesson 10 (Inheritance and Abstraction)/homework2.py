class Addition :
    def __init__(self, a, x,y):
        self.a = a
        self.x = x
        self.y = y


        def result( self):
            self.num = self.x + self.y + self.a
            return self.num
        
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
a = int(input("Enter the third number: "))
Sum = Addition(a,x,y)

sum = Sum.result()
print("The sum of the three numbers is:", sum)