def myfunction(n):

    for i in range(0,n+1):
        print("First loop")

    j = i 
    while(j<n+1):
        print("Second loop")
        j = j*2

    for i in range(0,100):
        print("Third loop")

print("Funtion above willt ake time ")
print(" 0(n) + 0(log n) + 0(100) ")

