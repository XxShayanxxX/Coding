#python program to change the cases of letters in a string 
def changeTheCase(s):
    result = " "
    for i in s:
        #chaning lower case to upper case 
        if i.islower():
            result = result + i.upper()
        #upper case to lower case
        if i.isupper():
            result = result + i.lower()

    return result 

#drivers code 
inp = input("Enter String: ")
print("String after change lower case to upper case vice-versa")
print(changeTheCase(inp))