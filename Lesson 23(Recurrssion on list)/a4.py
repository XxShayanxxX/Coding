#recursively find the largest number iin array 
def maxarray(a):

    #Calculate length of array 
    length = len(a)

    # IF array length is 1 just return the element
    if length == 1:
        return a[0]
    

    #Returen the largest number among cureent llargest and cureent element 
    return max(a[0],maxarray(a[1:]))

a = [ 1, 243 , 4234 , 52333 ,5 , 23 ]

#Display results 
print("Largest element in array : ", maxarray(a))