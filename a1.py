#Program for intersections sort
A = [10,5,13,8,2]
for i in range(1,len(A)):

    value = A[i]

    #Move elements of A[0,,,i-1],that are greater than value , to one position ahead of their current position

    j = i - 1
    while j >= 0 and value <A[j]:
        A[j+1] = A[j]

        j -= 1
        A[j+1] = value


    #Drivers code 

print("Sorted array :")
for i in range(len(A)):
    print("%d" %A[i],end =" ")