def reco_fibur(n):

    if n <= 1 :
        return n 
    
    else: 
        return(reco_fibur(n-1) + reco_fibur(n-2))
    
nterms = int(input("Enter the number of terms: "))
if nterms <= 0:
        print("Please enter a positive integer")    

else: 
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(reco_fibur(i))