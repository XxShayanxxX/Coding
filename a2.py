#initalizing matrices 
x = [[8,2,9,7],
     [4,1,9,5],
     [1,4,8,2],
     [8,6,4,8]]

answer = 0 

for i in range(len(x)):
    for j in range(len(x[0])):
        #coloum-wise sum of items
        answer = answer + x[j][i]
    #print the coloum sum 

    print(answer, end=' ')
    answer = 0 
