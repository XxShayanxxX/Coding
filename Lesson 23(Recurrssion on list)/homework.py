#def lengthcalculate(a):

#   count = 0 
##   for _ in a:
#      count += 1 
#   return count

#length = lengthcalculate(list)
#print("The length of the list is :",length)


def calclist(a):
    if a == []:
        return 0 
    else :
        return 1 + calclist(a[1:])
    
list = [1,3,4,2,4,2,43,4,23,21]
length = calclist(list)
print("The length of the list is :", length)
    


# def list_length(my_list):
#    if not my_list:
#    return 0
#   return 1 + list_length(my_list[1::2]) + list_length(my_list[2::2])

#my_list = [1, 2, 3, 11, 34, 52, 78]
#print("The list is :")
#print(my_list)
#print("The length of the string is : ")
#print(list_length(my_list))
