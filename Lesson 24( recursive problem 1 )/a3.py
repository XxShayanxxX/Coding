n = int(input("ENter a number"))

def checkpower(n):
    # if  is less than equal to 00 just say no
    if(n<=0):
        return False
    
    #if we reach lowest power of n just retuirn true 
    if(n == 1):
        return True
    if(n% 4 == 0):
        return checkpower(n/4)
    return False
if(checkpower(n)):
    print("Power of 4 ")
else:
    print("not power of 4 :C")