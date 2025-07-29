#Program to sort 0s and 1s in the asrray 

def sortZerone(A,n):

    #Count the number of zero in an array \
    count = 0 
    
    for i in range(0,n):
        if(A[i] == 0 ):
            count = count + 1 

    #Filling the A with 0 until count 
    for i in range(0,count):
        A[i] = 0 

    #Filling the remaining space with 1 
    for i in range(count,n):
        A[i] = 1


#Drivers code 
A = [0,1,0,1,1,1,1]
n = len(A)

sortZerone(A,n)
print("Sorted array ", end = ' ')
for i in range(0,n):
    print(A[i],end = ' ')