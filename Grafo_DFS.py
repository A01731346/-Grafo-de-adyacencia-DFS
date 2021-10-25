  # Ethienne J. Cruz Gutiérrez | A01731346
  # Análisis y diseño de algoritmos
  # Grafo de adyacencia DFS
   
  # Instrucciones: Implementar DFS sobre un grafo que utilice matrices de adyacencia en lugar de listas ligadas


from pyvis.network import Network

class Graph:
    adj = []
    def __init__(self, v, e):

        self.v = v
        self.e = e
        Graph.adj = [[0 for i in range(v)]
                     for j in range(v)]

    def addEdge(self, start, e):

        Graph.adj[start][e] = 1
        Graph.adj[e][start] = 1

    def DFS(self, start, visited, nodes):
        nodes.append(start)
        visited[start] = True
        for i in range(self.v):
            if (Graph.adj[start][i] == 1 and
                    (not visited[i])):
                self.DFS(i, visited, nodes)

    def printGraphMatrix(self):
        for m in Graph.adj:
            print(m)
        print("")

v, e = 6, 6

G = Graph(v, e)
G.addEdge(0, 1)
G.addEdge(1, 2)
G.addEdge(2, 3)
G.addEdge(3, 4)
G.addEdge(4, 5)
G.addEdge(5, 0)

visited = [False] * v
nodes = []

G.DFS(0, visited, nodes);
print("Matriz de adyacencia")
G.printGraphMatrix()

print("\nImpresión resultado del DFS: ")
print(nodes)

net = Network()
net.add_nodes(nodes)

net.add_edge(0, 1, weight=1)
net.add_edge(1, 2, weight=1)
net.add_edge(2, 3, weight=1)
net.add_edge(3, 4, weight=1)
net.add_edge(4, 5, weight=1)
net.add_edge(5, 0, weight=1)


net.toggle_physics(True)
net.show('Grafo.html')
