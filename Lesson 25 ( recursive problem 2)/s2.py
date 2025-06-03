def paren(s,l,r,p,n):
    # if we reach end of list just print and return 
    if (p==2*n):
        for ss in s:
            print(ss,end='')
        print("\n")
        return
    #if left parentheses is greater thasn we can print right one 
    if(l>r):
        s[p]="}"
        paren(s,l,r+1,p+1,n)
        #Left parenthesis should not exceed n 
    if(l<n):
        s[p]="{"
        paren(s,l+1,r,p+1,n)

n = int(input("ENter a number : "))
            
s = [""]*2*n
print("\n")
paren(s,0,0,0,n)
 