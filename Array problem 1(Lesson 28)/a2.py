def rotation(a,n,a_size):
    for i in range(n):
        rotate(a,a_size)

#Rotate array to the left by 1 place 
def rotate(a,a_size):
    temp = a[0]
    for i in range(a_size - 1):
        a[i] = a[i + 1]
    a[a_size-1] = temp 

def printArray(a, a_size):
    for i in range(a_size):
        print("% d" % a[i],end=" ")
    print("\n")


a = [ 12,12,12,31,312,134,25,436,5464655,3234]
printArray(a,len(a))
rotation(a,2,len(a))
printArray(a,len(a))