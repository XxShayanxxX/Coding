from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edges(self,u,v):
        self.graph[u].append(v)

    def bfs(self,start):
        visited = [False] * (max(self.graph)+1)
        queue = []

        queue.append(start)
        visited[start] = True 

        while queue:
            node = queue.pop(0)
            print(node,end=' ')

            for neighbour in self.graph[node]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour] = True

#Test the BFS algorithm 
if __name__ == "__main__":
    g = Graph()

    #Add edges to the graph 
    g.add_edges(0,1)
    g.add_edges(0,2)
    g.add_edges(1,2)
    g.add_edges(2,0)
    g.add_edges(2,3)
    g.add_edges(3,3)

    print("BSF traversal starting from vertex 2")

    g.bfs(2)