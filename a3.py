#function to count the number of words in a string 

def countwords(n):
    count = 0 

    n = n.strip()
    for i in range(len(n)):
        if n[i] == " ":
            count += 1 
    
    return count + 1


#drivers code 
inp = input("Enter a string : ")
print("Number of words : ", countwords(inp))