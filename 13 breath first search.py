class Vertex:
    def __init__(self, n):
        self.name = n
        self.edges = []
        self.distance = None
        self.visited = False

class Graph:
    verteces = {}
    def add_vertex(self, vertex):
        v = Vertex(vertex)
        if vertex not in self.verteces:
            self.verteces[v.name] = v
            return True
        else:
            return False
    def add_edges(self, m, n):
        if m in self.verteces and n in self.verteces:
            self.verteces[m].edges.append(n)
            self.verteces[m].edges.sort()
            self.verteces[n].edges.append(m)
            self.verteces[n].edges.sort()
            return True
        else:
            return False
    def print(self):
        for i in self.verteces:
            print(i + ' ' + str(self.verteces[i].edges))
    def breath_first_search(self, vertex):
        for i in self.verteces:
            self.verteces[i].visited = False
        self.verteces[vertex].distance = 0
        queue = []
        queue.append(vertex)
        self.verteces[vertex].visited = True
        while queue:
            a = queue.pop(0)
            print(a + ' '+  str(self.verteces[a].distance), end = ' ')
            for i in self.verteces[a].edges:
                if self.verteces[i].visited == False:
                    queue.append(i)
                    self.verteces[i].visited = True
                    if self.verteces[i].distance is None:
                        self.verteces[i].distance = self.verteces[a].distance + 1

g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_edges('A', 'B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('F')
g.add_edges('A','C')
g.add_edges('A', 'F')
g.add_edges('F','D')
g.print()
g.breath_first_search('A')