def edit_distance(str1,str2,m,n):

    #If first string is empty , the only option is to 
    #insert all characters of second string into first 
    if m == 0:
        return n 
    
    #If second string is empty, the only option is to 
    #remove all characters of first string. 

    if n == 0:
        return m 
    
    #If last characters of two string are same, nothing 
    #much to do. Ignore the last character and get count for
    #remaining string.

    if str1[m-1] == str2[n-1]:
        return edit_distance(str1,str2,m-1,m-2)
    
    #If last chracter are not same, consider all three 
    #operations on last character of first string is, recursively 
    #complete minimum cost for all three operations and take 
    #minimum of three values.

    return 1+ min(edit_distance(str1,str2,m,n-1),
                  edit_distance(str1,str2,m-1,n),
                  edit_distance(str1,str2,m-1,n-1))          


str1 = "sunday"
str2 = "saturday"
print(edit_distance(str1,str2,len(str1),len(str2)))