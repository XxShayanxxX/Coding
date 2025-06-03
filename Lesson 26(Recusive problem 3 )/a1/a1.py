#Program to move n disks in TOwer of Hoai 

def Honai(n,a,b,c):
    if n == 1:
        print("Move disk 1 from rod", a,"to rod",b)
        return
    #move n-1 disk from a to b 
    Honai(n-1,a,c,b)
    print("Move disk",n,"from rod",a,"to rod b")
    Honai(n-1,c,b,a)


n = 3
Honai(n,'A','C','B')