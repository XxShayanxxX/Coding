def removowels(s):
    result = ""
    #list containing vowels 

    li = ['a','e','i','o','u']
    for i in range(len(s)):
        #checking the precense of vowels in a string 
        if s[i] in li:

            #removing vowels 
            result = result + ""

        else:
            result = result + s[i]

    return result



#drivers code
inp = input("enter a string: ")
print(removowels(inp))
        