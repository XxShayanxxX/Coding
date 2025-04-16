# find facvtor of user input 
# checks % by the number to find the factors\

def print_factors(num):
    print("The factores of", num, "are:")
    for i in range(1,num+1):
        if num % i == 0 :
            print(i)

# taking input from the user 
numberinput = int(input("enter a number"))

# calling the function 
print_factors(numberinput)