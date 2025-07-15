#Program to reverse the same array 
A = [1,2,3,4,5,6]
#intializing start and end 
start = 0 
end = len(A) - 1
#reverse A from start to end 
while start < end :
    #swapping the elements of array to reverse it in same array 
    #same array 
    A[start],A[end] = A[end],A[start]
    start += 1 
    end -= 1 

#Drivers code 
print("Reverse array is : ")
print(A)