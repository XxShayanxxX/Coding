# Find if number is prime number 

from math import sqrt

num = int(input("Enter a number:"))
if num > 1:

    for i in range(2, int(sqrt(num)+1)):
                   
        if (num% i) == 0:
            print(num,"number is not a prime number")
            break
            
    else:
        print(num,"number is a prime number")

else:
    print(num,"number is not a prime number")