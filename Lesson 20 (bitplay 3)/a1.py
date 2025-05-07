def swap(a,b):

    a = a ^ b 
    b =  a ^ b
    a =  a ^ b 

def swap2(a,b):
    
    a = (a & b) + (a | b)
    b = a + (~b) + 1
    a = a + (~b) + 1

    print("After swapping",a,b)

swap(1,2)
swap2(1,2)