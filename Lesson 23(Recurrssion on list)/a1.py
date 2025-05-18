# Program to recursively check if a given array is sorted or not 

def checksorted(n):
    # Calculating the lenght of array 
    length = len(n)

    #If array length is 0,1 means we need not to check further 
    if length == 1 or length == 0:
        return True 
    
    #return true if both below conditons are true 
    return n[0] <= n[1] and checksorted(n[1:])

a = [1,2,3,4,5,6,7,8]

#Displaying result
if checksorted(a):
    print("YEs given array is sorted ")
else :
    print("No given array is not sorted")