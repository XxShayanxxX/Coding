def hcf(numS, numL):
    while(numS):
        numberstore = numS
        numS = numL % numS
        numL = numberstore
        
    return numL

numL = int(input("Enter the largest number:"))
numS = int(input("Enter the smallest number:"))

lcm = int((numS / hcf(numS,numL))*numL)
print("LCM is:", lcm)