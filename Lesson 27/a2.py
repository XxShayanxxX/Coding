# Minimum Function
def minE(a , size):
    temp = a[0]
    for i in range(1,size):
        temp = min(temp, a[i])
    return temp
    
# Maximum fuNCTION
def maxF(a , size):
    temp = a[0]
    for i in range(1,size):
        temp = max(temp,a[i])
    return temp
    
a = [12,1234,45,67,1]
size = len(a)
print("Minimum elemnt of array = ", minE(a,size))
print("Maximum elemnt of arrAY =", maxF(a,size))