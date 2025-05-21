n = int(input("Enter a number : "))

def checkpower2(n):
    if (n<=0):
        return False
    
    if (n == 1):
        return True
    
    if (n % 2 == 0):
        return checkpower2(n/2)
    return False
    

if(checkpower2(n)):
    print("The number is power of 2")

else : 
    print("Number is not power of 2 ")