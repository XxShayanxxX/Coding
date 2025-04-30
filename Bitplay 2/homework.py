def reverseBits(numbver):

    reversed = 0 

    while numbver > 0:

        reversed = reversed << 1 

        if numbver & 1 == 1:
            reversed = reversed ^ 1


        numbver == numbver >> 1

    return reversed

numbver = int(input("Enter a number:"))
print("Number with r3versed bits is:", reverseBits(numbver))
