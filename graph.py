"""Graph module"""
import math


class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = {}
        self.distance = math.inf
        self.visited = False

    def addEdgeTo(self, src, weight):
        self.edges[src] = weight

    def get_neighbors(self):
        return self.edges.keys()


class Graph():
    def __init__(self):
        self.edge_count = 0
        self.vertices = dict()
        self.size = 0

    def add_vertex(self, label):
        self.vertices[label] = Vertex(label)
        self.size += 1
        return self

    def add_edge(self, src, dest, w):
        src_vertex = self.vertices[src]
        dest_vertex = self.vertices[dest]
        src_vertex.addEdgeTo(dest_vertex, w)
        self.edge_count += 1
        return self


    def get_weight(self, src, dest):
        print("")

    def dfs(self, starting_vertex):
        print("")

    def bfs(self, starting_vertex):
        print("")

    def dijkstra_shortest_path(self, src, dest=None):
        for v in self.vertices.values():
            v.dist = math.inf
            v.visited = False
        self.vertices[src].distance = 0

        while False in [x.visited for x in self.vertices.values()]:
            current_searchable = []
            for vertex in self.vertices.values():
                if not vertex.visited:
                    current_searchable.append(vertex)
            distances = [x.distance for x in current_searchable]
            print(distances)
            print([x.label for x in current_searchable])
            for vertex in current_searchable:
                if vertex.distance == min(distances):
                    node_to_visit = vertex
                    node_to_visit.visited = True
                    adjacent = node_to_visit.get_neighbors()
                    for neighbor in adjacent:
                        print("Here1")
                        print([x.label for x in adjacent])
                        if (node_to_visit.distance + node_to_visit.edges[neighbor]) < neighbor.distance:
                            print("Here")
                            neighbor.distance = node_to_visit.distance + node_to_visit.edges[neighbor]
        for each in self.vertices.values():
            print(f"{each.label} {each.distance}")






    def __str__(self):
        print("")


g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")

g.add_edge("A", "B", 2)
g.add_edge("A", "F", 9)

g.add_edge("B", "F", 6)
g.add_edge("B", "D", 15)
g.add_edge("B", "C", 8)

g.add_edge("C", "D", 1)

g.add_edge("E", "C", 7)
g.add_edge("E", "D", 3)

g.add_edge("F", "E", 3)

g.dijkstra_shortest_path("A")
