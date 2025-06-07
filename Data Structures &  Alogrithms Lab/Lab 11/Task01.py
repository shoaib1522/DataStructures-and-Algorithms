class GraphNode:
    def __init__(self, vertex=0, next_node=None):
        self.vertex = vertex
        self.next = next_node

class Graph:
    MAX = 10 
    def __init__(self):
        self.headnodes = [None] * self.MAX 
        self.n = 0  
        self.visited = [False] * self.MAX  
    def initialize_visited(self):
        self.visited = [False] * self.MAX  
    def addVertex(self, vertex):
        if self.headnodes[vertex] is None:
            self.headnodes[vertex] = GraphNode(vertex)
            self.n += 1
    def removeVertex(self, vertex):
        if self.headnodes[vertex] is not None:
            self.headnodes[vertex] = None
            self.n -= 1
            for i in range(self.MAX):
                if self.headnodes[i] is not None:
                    self.removeEdge(i, vertex)
    def addEdge(self, v1, vertex2):
        if self.headnodes[v1] is None or self.headnodes[vertex2] is None:
            return
        newNode = GraphNode(vertex2)
        newNode.next = self.headnodes[v1].next
        self.headnodes[v1].next = newNode
    def removeEdge(self, v1, vertex2):
        if self.headnodes[v1] is None:
            return
        temp = self.headnodes[v1]
        prev = None
        while temp is not None and temp.vertex != vertex2:
            prev = temp
            temp = temp.next
        if temp is not None:
            if prev is None:
                self.headnodes[v1].next = temp.next
            else:
                prev.next = temp.next
    def vertexExists(self, vertex):
        return self.headnodes[vertex] is not None
    def printGraph(self):
        for i in range(self.MAX):
            if self.headnodes[i] is not None:
                print(f"{i}: ", end="")
                temp = self.headnodes[i].next
                while temp is not None:
                    print(f" {temp.vertex}", end=", ")
                    temp = temp.next
                print()
    def dfs(self, vertex):
        if not self.vertexExists(vertex):
            return
        self.visited[vertex] = True
        print(vertex, end=" ")
        temp = self.headnodes[vertex].next
        while temp is not None:
            if not self.visited[temp.vertex]:
                self.dfs(temp.vertex)
            temp = temp.next
    def bfs(self, vertex):
        if not self.vertexExists(vertex):
            return
        queue = []
        self.visited[vertex] = True
        queue.append(vertex)
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")
            temp = self.headnodes[vertex].next
            while temp is not None:
                if not self.visited[temp.vertex]:
                    self.visited[temp.vertex] = True
                    queue.append(temp.vertex)
                temp = temp.next

g = Graph()
for i in range(6):
    g.addVertex(i)
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 5)
g.addEdge(3, 4)
g.addEdge(4, 2)
g.addEdge(4, 5)
g.addEdge(5, 1)
g.printGraph()
print("DFS:")
g.dfs(0)
print()
g.initialize_visited()
print("BFS: ")
g.bfs(0)
print()
