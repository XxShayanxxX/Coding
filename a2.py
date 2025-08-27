def reverse(s):
    n = len(s)

    li = list(s)
    for i in range(n//2):

        li[i]   ,li[n-i-1] = li[n-i-1],li[i]
    return "".join(li)
#function to check the string is palindrome 
def checkpalindrome(s):
    #ignoring case
    s = s.lower()
    rev_string = reverse(s)
    if s == rev_string:
        return True 
    else:
        return False
    

#drivers code
inp = input("Enter string: ")
print(checkpalindrome(inp))