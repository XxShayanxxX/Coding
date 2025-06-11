# Program to find tthe max profit you can get from buying and selling stocks, You are given an array with stocks price for severn days, and you can buy and sell any day 

def calcProfit(arr,a_size):


    profit = 0 
    for i in range(1,a_size):

        #If the current elemenbt is greater than last element then we will but the previous day and sell it the current day
        if arr[i] > arr[i-1]:
            #Calculate profit 
            profit += arr[i] - arr[i-1]

        return profit 
    

#Prices for 7 days 
prices = [638,864,247,325,257,745,245]
profit = calcProfit(prices,len(prices))
print("THe max profit is :", profit)