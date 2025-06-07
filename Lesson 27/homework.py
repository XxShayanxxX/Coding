#Reverse function
def reverse(arr , start, end):
    while start < end:
        arr[ start], arr[end] = arr[ end], arr[ start]
        start += 1
        end -= 1 

arr = [ 1,2,3,4,5,6,7,8,9]
print("The actual array is \n")
print(arr)
print("The reversed array is : \n", reverse(arr,0,8))
print(arr)