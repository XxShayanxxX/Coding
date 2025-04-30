def printTwoOdd(arr, size):
    #xorof will hold xor of the 2 odd occurring elements
    xorof = arr[0]
    x = 0 
    y = 0

    #This will hold the rightmost set bit from xorof
    setbit = 0 

    for i in range(1, size):
        xorof = xorof ^ arr[i]

    setbit  = xorof & ~(xorof -1)

    # If number is having set bit at location we need then XOR it with x else with y
    for i in range(size):
        if(arr[i] & setbit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]

    print("The two odd occuring elements are :",x ,"&", y )

arr = []

arr_size = int(input("Enter siz of arrayy: "))
for i in range(0,arr_size):
    z = int(input("Enter a number:"))
    arr.append(z)

printTwoOdd(arr, arr_size)