#directed graph
class Vertex:
    def __init__(self, n):
        self.name = n
        self.weights = []
        self.neighbors = []
        self.visited = False
        self.distance = None

class Graph:
    vertices = {}
    index = {}
    stat = {}
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = Vertex(vertex)
            self.index[vertex] = len(self.vertices) - 1
            self.vertices[vertex].weights = [0]*len(self.vertices)
            for i in self.vertices:
                if i != vertex:
                    self.vertices[i].weights.append(0)
            return True
        else:
            return False
    def add_edges(self, m, n, weight = 1):
        if m in self.vertices and n in self.vertices:
            self.vertices[m].weights[self.index[n]] = weight
            self.vertices[n].weights[self.index[m]] = weight
            self.vertices[m].neighbors.append(n)
            self.vertices[n].neighbors.append(m)
    def print(self):
        for i in self.vertices:
            print(i + ' ' + str(self.vertices[i].weights) + ' '+ str(self.index[i]))
    def dijkstra(self, s):
        for i in self.vertices:
            self.vertices[i].visited = False
            self.distance = None
        queue = []
        queue.append(s)
        self.vertices[s].distance = 0
        while queue:
            print(queue.pop(0))
            for i in self.vertices[queue.pop(0)].neighbors:
                if i not in self.vertices[queue.pop(0)].visited:




g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_edges('A', 'B')
g.add_edges('C','A', 4)
g.print()