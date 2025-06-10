def leaders(a,a_size):
    #Right most is always a leaDER 
    currentmax = a[a_size - 1]
    print(currentmax)


    #Check from 2nd last element if it is greater than currentmax is yes that number is a leader and our currentmaxx too, 
    for i in range(a_size -2 , -1 , -1):
        if currentmax < a[i]:
            print(a[i])
            currentmax = a[i]



a = [ 16, 17 , 4 , 3, 5 , 245]
leaders(a, len(a))
