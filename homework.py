def part(A,low,high):

    pivot = A[high]

    i = low -1

    for j in range(low,high):
        if A[j]  <= pivot:

            i += 1 
            (A[i],A[j]) = (A[j],A[i])

    A[i +1 ],A[high] = A[high],A[i+1]
 
    return i + 1


def quicksort(A,low,high):
    if low < high:

        p = part(A,low,high)

        quicksort(A,low,p - 1)

        quicksort(A,p +1,high)

n = int(input("Enter the elements : "))
A = []
for i in range(n):
    elements = int(input("Enter a number : "))
    A.append(elements)

quicksort(A,0,len(A)-1)

print(A)