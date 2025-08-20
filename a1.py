#intitalizing matrices 
x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

answer = [[0,0,0],
          [0,0,0],
          [0,0,0]]


for i in range(len(x)):
    for j in range(len(x[0])):
        #transpose matrix 
        answer[i][j] = x[j][i]

for r in answer:
    print(r)

    