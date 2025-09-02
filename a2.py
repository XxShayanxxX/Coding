# An anagram is a string formed by rearranging the letters of another string.
# function to count the frequency of each
# character of a string 
def frequency(s):
    #creating a dictonary to store the frequency of each character 
    s = s.lower()
    d = {}

    for i in range(len(s)):
        #checking if the character is already 
        #in the dictonary 

        if s[i] in d.keys():
            d[s[i]] += 1 
            
        else:
            d[s[i]] = 1 

    return d 

#function to check Anagram strings 
def checkAnagram(s1,s2):
    d_s1 = frequency(s1)
    d_s2 = frequency(s2)

    if d_s1 == d_s2:
        return True 
    else:
        return False
    
#drivers code 
inp1 = input("Enter a string 1: ")
inp2 = input("Enter a string 2: ")

print(checkAnagram(inp1,inp2))
