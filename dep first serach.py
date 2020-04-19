class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = []
        self.visited = False
        self.first = 0
        self.second = 0

class Graph:
    vertices = {}
    time = 0
    def add_vertex(self, vertex):
        v = Vertex(vertex)
        if vertex not in self.vertices:
            self.vertices[vertex] = v
            return True
        else:
            return False
    def add_edges(self, m, n):
        if m in self.vertices and n in self.vertices:
            self.vertices[m].neighbors.append(n)
            self.vertices[m].neighbors.sort()
            self.vertices[n].neighbors.append(m)
            self.vertices[n].neighbors.sort()
            return True
        else:
            return False
    def print(self):
        for i in self.vertices:
            print(i + ' ' + str(self.vertices[i].neighbors)+ ' ' + str(self.vertices[i].first)+ '/'+ str(self.vertices[i].second))
    def dep_travesal(self, s):
        self.vertices[s].visited = True
        self.vertices[s].first += self.time
        self.time += 1
        for i in self.vertices[s].neighbors:
            if self.vertices[i].visited == False:
                self.dep_travesal(i)
        self.vertices[s].visited = False
        self.vertices[s].second = self.time
        self.time += 1
    def dep(self, s):
        self.time = 1
        self.dep_travesal(s)

g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_edges('A','B')
g.add_vertex('C')
g.add_edges('C', 'A')
g.add_vertex('F')
g.add_vertex('D')
g.add_edges('C','F')
g.add_edges('C','D')
g.dep('A')
g.print()
