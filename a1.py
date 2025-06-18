def equibrimPoint(arr):
    leftsidesum = 0 
    rightsidesum = 0 
    n = len(arr)


    #Go to each indx of the array and check if it an equiliubrium point 
    for i in range(n):
        leftsidesum = 0 
        rightsidesum = 0 
         

         #get left sum 
        for j in range(i):
            leftsidesum += arr[j]

        #get right sum 
        for j in range(i + 1,n):
            rightsidesum += arr[j]


        # if leftsum and rightsum are same , 
        #then we are done 
        if leftsidesum == rightsidesum:
            return i 
        

    return -1

arr = [-4,6,2,0,0,1,1]
print("Element :", arr[equibrimPoint(arr)])
           