def divide(ourDividend, ourDivisor):
  
    sign = (-1 if (ourDividend < 0 ) ^ (ourDivisor < 0)  else 1)
    
    ourDivisor = abs(ourDivisor);
    ourDividend = abs(ourDividend);

    quotent = 0
    temp = 0 

    for i in range(31, -1 ,-1):

        if(temp + (ourDivisor << i) <= ourDividend ):
            temp += ourDivisor << i 
            quotent |= 1 << i 

    if sign == - 1 :
        quotent = - quotent
    return quotent 

a = int(input("Enter the a for a/b :"))
b = int(input("Enter the b for a/b :"))
print(divide(a,b))