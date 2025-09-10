#program to check if 
# a string is a substring  of other 

#check if s1 is a substring of string 2 
def isSubstring(s1,s2):
    if s1 in s2:
        return s2.index(s1)
    return -1 


#drivers code 
if __name__ == "__main__":
    s1 = "Welcome"
    s2 = "Welcome to codingal"
    result = isSubstring(s1,s2)
    if result == -1 :
        print("Not present ")
    else:
        print("Present at index " + str(result))