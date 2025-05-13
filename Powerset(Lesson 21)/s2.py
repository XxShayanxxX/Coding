def totalFlip(num1, num2):
    # Var to count flips required
    flips = 0 

    # Get the last bit of both numbers and check of both same if yes no flip required else flip is required
    while(num1 > 0 or num2 > 0 ):
        t1 = (num1 & 1)
        t2 = (num2 & 1)
        if (t1 != t2):
            flips += 1 

            #Right shift btoh numbers
            num1 >>= 1
            num2 >>= 1

        return flips
    
num1 = int(input("Enter a number : "))
num2 = int(input("Enter a second number :"))

print("\n Number of flipes need : ", totalFlip(num1,num2))