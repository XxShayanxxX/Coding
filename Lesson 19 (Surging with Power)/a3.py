def computerPower(x,y):

    result = 1

    while y > 0:
        if y % 2 == 0:
            x = x* x
            y >>= 1

        else:
            result = result * x 
            y = y - 1

    return result

x = int(input("Enter a number:"))
y = int(input("Enter the 2nd number:"))

print("Total is:", computerPower(x,y))

