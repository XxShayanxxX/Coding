def countways(maze):
    R,C = len(maze),len(maze[0])
    dp = [[0]*C for _ in range(R)]

    #Start point 

    dp[0][0] = 1 if maze[0][0] == 1 else 0

    for i in range(R):
        for j in range(C):
            if maze[i][j] == 0:
                continue

        if i > 0:
            dp[i][j]
