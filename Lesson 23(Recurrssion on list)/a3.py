#recursively calculate the sum of all em=lements of tthe given list 
def arraytottalsum(a):
    #Calculating length of array 
    length = len(a)

    #If array length is 1 just return the element 
    if length == 1:
        return a[0]
    

    #Return curent element and recieve sum
    return a[0] + arraytottalsum(a[1:])

a = [1,2,3,4,6]

# display result 
print("Araay total sum:", arraytottalsum(a))