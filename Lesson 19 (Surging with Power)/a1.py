def power2(number):
    #A the power of bit will only have 1 set bit, then n - 1 & n will always be 0
    if (number == 0):
        return 0 
    if  (number & (~(number - 1))) == number:
        return 1
    return 0 

number = int(input("Enter a number: "))

if (power2(number)):
    print("The number is a power of 2")
else:
    print("The number is not a power of 2")
