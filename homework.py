x = [[8,2,5,6],
     [3,1,9,5],
     [1,4,8,2],
     [8,6,4,8]]

for i in range(len(x)):
    row_sum = 0 
    for j in range(len(x[0])):
        row_sum = row_sum + x[i][j]

    print(row_sum,end=' ')
    
    





