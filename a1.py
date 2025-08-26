#function to reverse the string 
def reverse(s):
    n = len(s)

    #converting string to list 
    li = list(s)
    for i in range(n//2):
        #swapping first and last,second and second last and so on 
        li[i],li[n-i-1] = li[n-i-1],li[i]
    return "".join(li)


#drivers code 
inp = input("Enter string : ")
print(reverse(inp))