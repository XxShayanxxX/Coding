def rmv(text):
    words = text.split()
    result = []

    for letter in words:
        if letter not in result:
            result.append(letter)

    return " ".join(result)

#drivers code 

inp = input("Enter a string : ")
print(rmv(inp))


            