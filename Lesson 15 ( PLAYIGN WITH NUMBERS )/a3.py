number1 = int(input("enter the first number: "))
number2 = int(input("enter the second number:"))

a = number1 
b = number2

while b!= 0 :
 a,b = b, a % b


hcf = a
lcm = number1 * number2 // hcf 

print("Lcm :", lcm)

