def fac(n):
    if(n ==1 or n == 0 ):
        return 1 
    return n*fac(n-1)

num = int(input("Enter a number : "))
print("The factorial of the given number is : ", fac(num))