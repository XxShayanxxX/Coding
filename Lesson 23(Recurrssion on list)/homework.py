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
    
list = [1,3,4,2,4,2,43,4]
length = calclist(list)
print("The length of the list is :", length)
    
