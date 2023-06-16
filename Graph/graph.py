# class GraphList:
#     def __init__(self) -> None:
#         self.dict = dict()

#     def display(self):
#         for vertex in self.dict:
#             print(vertex, ":", self.dict[vertex])

#     def add_vertex(self, vertex):
#         if vertex not in self.dict.keys():
#             self.dict[vertex] = []
#             return True
#         return False

#     def add_edge(self, v1, v2):
#         if v1 in self.dict.keys() and v2 in self.dict.keys():
#             self.dict[v1].append(v2)
#             self.dict[v2].append(v1)
#             return True

#         return False

#     def remove_edge(self, v1, v2):
#         if v1 in self.dict.keys() and v2 in self.dict.keys():
#             self.dict[v1].remove(v2)
#             self.dict[v2].remove(v1)
#             return True

#         return False

#     def remove_vertex(self, vertex):
#         if vertex in self.dict.keys():
#             for other_vertex in self.dict[vertex]:
#                 self.dict[other_vertex].remove(vertex)

#             del self.dict[vertex]

#             return True

#         return False


# graph = GraphList()

# graph.add_vertex(40)
# graph.add_vertex(50)

# graph.add_edge(40, 50)
# graph.display()

# graph.remove_edge(40, 50)
# graph.display()

class GraphMatrix:
    def __init__(self):
        self.num_of_vertices = 0
        self.dict = dict()
        self.vertices = []

    def display(self):
        print(' ', '_' * (self.num_of_vertices * 2))
        for key in self.dict:
            print(f'{key} :', self.dict[key])

    def add_vertex(self, vertex):
        if vertex in self.vertices:
            print(f'{vertex} is already in the graph!')

        self.num_of_vertices += 1
        self.dict[vertex] = dict()
        self.vertices.append(vertex)

        for inner_vertex in self.vertices:
            self.dict[vertex][inner_vertex] = 0
            self.dict[inner_vertex][vertex] = 0

        print(f'Added a new node: {vertex}')

    def remove_node(self, vertex):
        if vertex not in self.vertices:
            print(f'{vertex} not in graph!')
            return

        self.dict.pop(vertex)

        for row in self.dict.values():
            row.pop(vertex)

        self.vertices.remove(vertex)
        self.num_of_vertices -= 1

    def add_edge(self, a, b):
        if a not in self.vertices and b not in self.vertices:
            print("Nodes not in graph!")
            return

        if self.dict[a][b] == 1 and self.dict[b][a] == 1:
            print("Edge already established")
            return

        self.dict[a][b] = 1
        self.dict[b][a] = 1

    def remove_edge(self, a, b):
        if a not in self.vertices and b not in self.vertices:
            print("Nodes not in graph!")
            return

        if self.dict[a][b] == 0 and self.dict[b][a] == 0:
            print("No edge between vertices")
            return

        self.dict[a][b] = 0
        self.dict[b][a] = 0


g = GraphMatrix()
g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')
g.add_vertex('e')
g.add_vertex('f')
g.add_vertex('g')

g.add_edge('a', 'b')
# g.add_edge('c', 'a')
# g.add_edge('a', 'd')
# g.add_edge('b', 'e')
# g.add_edge('e', 'd')
# g.add_edge('e', 'g')
# g.add_edge('c', 'f')
# g.add_edge('f', 'd')
# g.add_edge('f', 'g')

g.display()


# def checkHP(adjM, list):
#     hp = []
#     for key in adjM:
#         if


# checkHP(g.dict, [])
