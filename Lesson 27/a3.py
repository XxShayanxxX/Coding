def printlarge(a,a_size):
    largest = secondlargest = -2147483648
    for i in range(a_size):

        # IF the current elemetn of the array is greather than out current largest number, then replace 
        if(a[i] > largest):

            secondLargest = largest
            largest = a[i]



            # IF current element is less than current largest but greater than second largest then replace the number
        elif ( a[i] > secondlargest and a [ i] != largest ):
            secondlargest = a[ i]


    print(secondlargest)

a = [1,23,4,5,6,7,8,9]
a_size = len(a)
printlarge(a,a_size)
