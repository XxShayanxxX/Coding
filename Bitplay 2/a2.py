def oddoccuring(arr):

#Initialize result  
    res = 0 

    # Transverse the array 
    for element in arr:
        #Xor the result 
        res = res ^ element

    return res

#Initialize the array 
arr = [ ]

# Take array size as input
n = int(input("Enter the size of the array : "))

# Take array elements as input 
while(n):
    num = int(input("Enter a number :"))
    arr.append(num)
    n-=1

print("\n Odd occuring number is : ", oddoccuring(arr))
