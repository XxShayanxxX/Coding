def max1(number):

    count = 0 

    while(number!=0):

        number = number & (number << 1)

        count = count + 1

    return count 

number = int(input('Enter a number:'))
print("The longest consecutive number 1 :  ", max1(number))