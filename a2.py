def count(coins,n,sum):

    # If sum is 0 then there is 1 
    # solution (do not include any coins)
    if (sum == 0):
        return 1 
    
    # If sum is less than 0 then no 
    # solution exsist 
    if (sum < 0):
        return 0 
    
    if (n <= 0):
        return 0     
    #count is sum of solution (i)
    # including coins[n-1] (ii) excluding coins [n-1]
    return count(coins,n-1,sum) + count(coins,n,sum-coins[n-1])

#Driver program to test above function 
coins = [1,2,3]
n = len(coins)
print(count(coins,n,4))
