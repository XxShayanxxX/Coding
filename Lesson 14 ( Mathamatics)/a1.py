# Program to find ArmStrong number 

#Take input from user 
number=  int(input("Enter a number:"))

#calculate the number of digits 
digits = len(str(number))
# initialize result varibale 
resultnum = 0 

temp = number 
while temp > 0 :
    digit = temp %  10    
    resultnum += digit ** digits
    temp//=10

if number == resultnum:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")


