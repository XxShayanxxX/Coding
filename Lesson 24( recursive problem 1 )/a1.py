#Program to reverse a number using recurrsion 

def reverserNumber(n):
    if(n > 0):
        # If input number is not 0 then get the last digit and add to the current reversed number recieverd 
        last = n % 10 
        if(n//10 >0):
            current_num = reverserNumber((int)(n//10))
            return last*pow(10,len(str(current_num))) + current_num
        return n 
    
num = int(input("Enter a number  "))
print("Reversed : ", reverserNumber(num))
