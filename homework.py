def nonrep(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return s[i]
        
    return None


inp = input("Enter a string : ")
result = nonrep(inp)

if result:
    print("first non repeating characyer : ",result)

else:
    print("no non repeat ")


