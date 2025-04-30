#Program to check if user input number are equal without using any comparision operatior

def check_ifSame(num1, num2):

# User XOR operator as a^a is always 0 
    if((num1 ^ num2)) == 0:
        print("Both numbers are equal")

    else:
        print("Both numbers are not equal")

# Taking user input
num1 = int(input("Enter the first numeber:"))
num2 = int(input("Enter the second number:"))

check_ifSame(num1, num2)