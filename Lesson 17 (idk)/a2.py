def isEVENodd(n):
    if(n ^ 1 == n +1 ):
        return True
    else:
        return False


number = int(input("Enter a number: "))

if isEVENodd(number):
    print("The number is even")

else:   
    print("The number is odd")
    
