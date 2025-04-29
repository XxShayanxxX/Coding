# Program to check if the Nth bit is set or not set 
def setNor(number,n):
    # Make a mask varibale by left shifting 1 (k-1) times and check if (n AND mask) equals 1 or 0 
    if number & (1 << ( n - 1)):
        print("\nSET")
    else:
        print("\nNOTSET")


number = int(input("Enter a number :"))
n = int(input("Enter a bit"))
setNor(number,n)
    
