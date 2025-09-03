#Program to find lexicorographically next string 

def nextword(s):
    #If string is empty 
    if(s ==" "):
        return "a"
    

    #Find the first character from the right 
    #which is not a Z 
    i = len(s) - 1
    while(s[i] == 'z' and i >= 0 ):
        i -=1

    #If all characters are 'z' append 
    #if an 'a' at the end 
    if ( i == -1):
        s = s + 'a'

    #if there are soem non-z character 
    else:
        s = s.replace(s[i], chr(ord(s[i]) + 1), 1)

        return s 
    


#Drivers code 
inp = "Codingalz"
print(nextword(inp))