#An iterative python program to do DFS traversal from 
# a give source vertex. DFS(int s) traverses vertices 
#reachable from s.

#This class represents a graph using adjacency list represensation
class Graph:
    def __init__(self,V):#Constructor 
        self.V = V 
        self.adj = [[] for i in range(V)]#adjacency lists 

    def addEdge(self,v,w): #to add an edge to graph 
        self.adj[v].append(w)

    #prints all not yet visited vertices rechable from s 
    def DFS(self,s):
                #Intially mark all the vertices as not visitedd
        visited = [False for i in range(self.V)]

        #Create stack for DFS
        stack = []

        #Push the currwent source node.
        stack.append(s)

        while(len(stack)):
            #Pop a vertex fro stack and print it 
            s = stack[-1]
            stack.pop()

            #Stack may contai same vertex twice so  we need 
            #to print the popped item onlyt if it is not v
            #visited 

            if(not(visited[s])):
                print(s,end =" ")
                visited[s] = True 


            #Get all adjacent vertices of the popped vertex s 
            #If a adjacent hasd not be visited, then push it 
            #to the $tack

            for node in self.adj[s]:
                if (not visited[node]):
                    stack.append(node)

#Driver program to test methods of graph class 
g = Graph(5); #Total 5 vertices in graph 
g.addEdge(1,0)
g.addEdge(0,2)
g.addEdge(2,1)
g.addEdge(0,3)
g.addEdge(1,4)

print("Following is depth first traversal")
g.DFS(0)


        

        