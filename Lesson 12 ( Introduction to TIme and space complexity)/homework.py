def o1(n,m):
    total = n*m
    print("\n1 interation: 1")


def o2(n,m):
    total = 0 
    for i in range(1,n+1):
        total +=  m 
    print("N interations:  ",n)

m = int(input("Enter a for a*b:"))
n = int(input("Enter b for a*b:"))

o1(m, n)
o2(n, m)


