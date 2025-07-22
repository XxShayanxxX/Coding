#Quick sort in python 

#function to find the partition position 
def partition(A,low,high):

    #choosing the right element as pivot 
    pivot = A[high]

    #pointer for greater element 
    i = low - 1

    #compare each element with pivot 
    for j in range(low,high):
        if A[j] <= pivot:
            #if elements smaller than pivot is found 
            #swap it with greater element pointed by i 
            i = i + 1

            #swappinf element i with element at j 
            (A[i],A[j]) = (A[j],A[i])

    #swap the pivot element with the greatest element specified by i 
    (A[i+ 1],A[high]) = (A[high], A[i+1])

    #return the position from where the partation is done 
    return i + 1

#function to perform quicksort 
def quicksort(A,low,high):
    if low < high:


    #find pivot element such that 
    #element smaller than the pivot are on the left 
    #element greatert than the pivot are on the right 
     pi = partition(A,low,high)

    #recursive call on the left side of pivot 
     quicksort(A,low,pi - 1)

     #recursive call ont he right side of pivot 
     quicksort(A,pi+1,high)


A = [4,6,23,34,7,0,2,34,4,5,6,7,32]
print("unsorted array: ")
print(A)

n = len(A) - 1

quicksort(A,0,n)

print("sorted array: ")
print(A)
