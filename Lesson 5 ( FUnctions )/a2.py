def rec_factorial(n): 
    if n == 1 :
        return n 
    
    else: return n * rec_factorial(n-1)

num = int(input("Enter a number: "))

if num == 0 :
    print("The factorial of 0 is 1")

elif num < 0 :
    print("Factorial does not exist for negative numbers")

else : 
    print("The factorial of",num,"is",rec_factorial(num))

