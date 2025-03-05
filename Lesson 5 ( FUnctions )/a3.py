def add( x , y ):
    return x +  y 

def sub(x , y ):
    return x - y

def multiply(x , y):
    return x * y

def divide(x , y):
    return x / y 

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Sum :", add(num1,num2))
print("Difference :", sub(num1,num2))
print("Product :", multiply(num1,num2))
print("Divide :" , divide(num1,num2))   