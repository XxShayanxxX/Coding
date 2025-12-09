#Function to find the minimum 
#number of rabbits in the forest 

def minNumberOfRabbits(answer,N):

    #Initialize map
    map = {}

    #Traverse array and map arr[i]
    #to the number of occurrences 

    for a in range(N):

        if answer[a] in map:
            map[answer[a]] += 1 
        else:
            map[answer[a]] = 1 


    count = 0 

#Find the number groups and 
#no. of rabbits in each group 
    for a in map:

        x = a 
        y = map[a]

            #Find number of groups and 
            #multiply them with number 
            #of rabbits in each group 
        if(y %(x + 1) == 0):
            count = count + (y // (x + 1)) * (x + 1)
        else:
            count = count + ((y // (x + 1 ))+ 1) * (x + 1)

#count gives minimum number 
#of rabbits in the forest 
    return count

#Driver code 
arr = [2,2,0]
N = len(arr)

#Function Call 
print(minNumberOfRabbits(arr,N))

