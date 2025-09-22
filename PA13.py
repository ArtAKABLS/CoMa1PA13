class Vertex:
    def __init__(self, name):
        self.neighbours = []
        self.name = name

    def __str__(self):
        return f'Vertex {self.name} with neighbours {self.neighbours}.'

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour.name)


class Graph:
    def __init__(self):
        self.num_of_vertices = 0
        self.num_of_edges = 0
        self.graph_dict = {}

    def __iter__(self):
        for vertex in self.graph_dict:
            yield self.graph_dict[vertex]

    def __str__(self):
        return f'Graph with {self.num_of_vertices} vertices and {self.num_of_edges} edges.'

    def add_vertices(self, vertex_names):
        for vertex_name in vertex_names:
            if vertex_name not in self.graph_dict:
                self.graph_dict[vertex_name] = Vertex(vertex_name)
        self.num_of_vertices = len(self.graph_dict)
        # print(self.num_of_vertices)
        # print(self.graph_dict)

    def add_edge(self, vertex_name1, vertex_name2):

        # print(self.graph_dict)
        if vertex_name1 not in self.graph_dict:
            self.graph_dict[vertex_name1] = Vertex(vertex_name1)
            self.num_of_vertices += 1

        if vertex_name2 not in self.graph_dict:
            self.graph_dict[vertex_name2] = Vertex(vertex_name2)
            self.num_of_vertices += 1

        if vertex_name2 not in self.graph_dict[vertex_name1].neighbours \
                and vertex_name1 not in self.graph_dict[vertex_name2].neighbours and not vertex_name1 == vertex_name2:
            self.graph_dict[vertex_name1].add_neighbour(self.graph_dict[vertex_name2])
            self.graph_dict[vertex_name2].add_neighbour(self.graph_dict[vertex_name1])
            self.num_of_edges += 1
            # print(self.graph_dict[vertex_name1], self.graph_dict[vertex_name2])
        # print(self.num_of_vertices, self.num_of_edges)

    def get_max_degree(self):
        max_degree = 0
        for vertex in self.graph_dict:
            edges = len(self.graph_dict[vertex].neighbours)
            if edges > max_degree:
                max_degree = edges
        return max_degree
        # print(max_degree)


class Bipartite_Graph(Graph):
    def __init__(self):
        super().__init__()
        self.partition_A = []
        self.partition_B = []


    def __str__(self):
        return f'Bipartite graph with {len(self.partition_A)} vertices in A, {len(self.partition_B)} vertices in B ' \
               f'and {self.num_of_edges} edges.'

    def add_vertices(self, vertex_names, partition=None):
        # print(partition)
        if partition == 'A':
            self.partition_A.extend(vertex_names)
        if partition == 'B':
            self.partition_B.extend(vertex_names)
        super().add_vertices(vertex_names)

    def add_edge(self, vertex_nameA, vertex_nameB):
        if vertex_nameA not in self.partition_B and vertex_nameB not in self.partition_A:
            if vertex_nameA not in self.partition_A:
                self.partition_A.append(vertex_nameA)
            if vertex_nameB not in self.partition_B:
                self.partition_B.append(vertex_nameB)

            super().add_edge(vertex_nameA, vertex_nameB)
        #print(self.partition_A, self.partition_B)


'''G = Graph()
G.add_vertices(['u', 'v', 'w'])
G.add_edge('u', 'v')
G.add_edge('u', 'w')
G.get_max_degree()
for i in G:
    print(i)'''

'''u = Vertex('u')
v = Vertex('v')
w = Vertex('w')
u.add_neighbour(v)
u.add_neighbour(w)

print(u)
#print(v)
u = Vertex('u')
print(u)'''

'''B = Bipartite_Graph()
B.add_vertices(['a1', 'a2'], 'A')
B.add_vertices(['b1'], 'B')
B.add_edge('a1', 'b1')
B.add_edge('a2', 'b1')
print(B)'''

'''G = Graph()
G.add_edge("v4","v6")
G.add_edge("v5","v3")
G.add_edge("v3","v0")
G.add_edge("v3","v1")
print(G)
for i in G: print(i)
print(G.get_max_degree())'''


'''B = Bipartite_Graph()
B.add_vertices(['b0', 'b1', 'b2'],"B")
B.add_edge("a4","b0")
B.add_edge("a5","b2")
B.add_edge("a1","b2")
B.add_edge("a4","b2")
B.add_edge("a1","b0")
B.add_edge("a1","b1")
print(B)
for i in B: print(i)
print(B.get_max_degree())'''
