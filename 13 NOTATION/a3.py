def sq(n):
    iterations = 0
    for i in range(0,n):
        for j in range(0,n):
            iterations += 1
        print("*",end ="")
        iterations +=1
    print("")
print("\n with every n the time take and iterations will increase")

sq(5)
sq(23)
sq(32)

print("\n with even n the time taken equals to n^2")

