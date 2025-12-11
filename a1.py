#Number of vertices in the graph 
V = 4 

#Define infinity as the large 
#enough value. The value will be 
#used for vertices not connected to each other 
INI = 99999

#Solves all pair shortest pair 
#via Floyd Warshall Algorithm

def floydWarshall(graph):
    """ dist[][] will be the output
    matrix that will finally
        have the shortest distances
        between every pair of vertices"""
    """ initiallizing the solution matrix 
    same as input graph matrix 
    OR we can say that the initial 
    value of shortest distances 
    are based on shortest paths considering no
    intermideate vertices """

    dist = list(map(lambda i: list(map(lambda j: j,i)),graph))

    for i in range(V):

        #Pick all vertices as destination for the 
        #above picked source 
        for j in range(V):
        
                for k in range(V):
                     

                    #If vertex K is on the shortest path from 
                    # i to j, then update the value of dist[i][j]
                    dist[i][j] = min(dist[i][j],
                        dist[i][k] + dist[k][j]
                        )
    printSolution(dist)

# A utility function to print the solution 
def printSolution(dist):
    print("Following matrix shows the shortest diostances\ between every pair of vertices")
    for i in range(V):
         for j in range(V):
            if(dist[i][j] == INI):
               print("%7s" % ("INI"),end=" ")
            else:
                print("%7d\t" % (dist[i][j]),end=' ')
            if j == V-1:
                print()

                print("%7d\t" % (dist[i][j]), end=" ")
            if j == V-1:
                print()


#Drivers code 
if __name__ =="__main__":

    graph = [[0,5,INI,10],
        [INI,0,3,INI],
        [INI,INI,0,1],
        [INI,INI,INI,0]]
             
floydWarshall(graph)
