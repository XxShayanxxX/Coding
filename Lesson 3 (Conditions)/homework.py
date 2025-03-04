present = int(input("Enter a number: "))    
absent = int(input("Enter a number: ")) 

total = ( present - absent )/ present * 100
if total >= 75:
    print("You are allowed to sit in the exam")

else:
    print("You are not allowed to sit in the exam")
    