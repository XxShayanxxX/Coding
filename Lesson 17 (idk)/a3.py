# program to find the number of bits in a number

#Function taking our number as input
def numberofbits(n):
    count = 0 

    while(n):
        count += 1 
        n >>= 1


    return count

nummber = int(input("Enter a number:"))
print("Total bits", numberofbits(nummber))
              