# Program to print numbers from 1 to 10 using recurrsion 

# Recursive function that will accept n till it reaches 10 
def printto10(n):
    # Base case to stop the recursion
    if(n>10):
        return
    print(n)


    #Recursive call 1 --> 2 , 2--> 3 , 3 --> 4 and so on 
    printto10(n+1)


printto10(1)