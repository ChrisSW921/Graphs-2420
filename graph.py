"""Graph module"""
import math


class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = {}
        self.distance = math.inf
        self.visited = False

    def addEdgeTo(self, src, weight):
        """Add an edge to the vertex"""
        self.edges[src] = weight

    def get_neighbors(self):
        """Return list of neighbors of vertex"""
        return self.edges.keys()


class Graph():
    def __init__(self):
        self.edge_count = 0
        self.vertices = dict()
        self.size = 0
        self.dfs_list = []

    def add_vertex(self, label):
        """Add a vertex to graph"""
        self.vertices[label] = Vertex(label)
        self.size += 1
        return self

    def add_edge(self, src, dest, w):
        """Add an edge to graph"""
        src_vertex = self.vertices[src]
        dest_vertex = self.vertices[dest]
        src_vertex.addEdgeTo(dest_vertex, w)
        self.edge_count += 1
        return self

    def get_weight(self, src, dest):
        """Return weight of edge"""
        neighbors = self.vertices[src].get_neighbors()
        for neighbor in neighbors:
            if neighbor.label == dest:
                return self.vertices[src].edges[self.vertices[dest]]
        return math.inf

    def dfs_helper(self, vertice):
        """Recursion helper for dfs and bfs"""
        vertice.visited = True
        self.dfs_list.append(vertice.label)
        neighbors = vertice.edges.keys()
        for neighbor in neighbors:
            if not neighbor.visited:
                self.dfs_helper(neighbor)

    def bfs(self, starting_vertex):
        """bfs"""
        starting_vertex = self.vertices[starting_vertex]
        for vertice in self.vertices.values():
            vertice.visited = False
        self.dfs_list = []
        self.dfs_helper(starting_vertex)
        return self.dfs_list

    def dfs(self, starting_vertex):
        """dfs"""
        starting_vertex = self.vertices[starting_vertex]
        for vertice in self.vertices.values():
            vertice.visited = False
        self.dfs_list = []
        self.dfs_helper(starting_vertex)
        return self.dfs_list

    def get_all_edges(self):
        """Return all edges in graph"""
        all_edges = {}
        for vertice in self.vertices.values():
            for vert in vertice.edges.keys():
                all_edges[(vertice.label, vert.label)] = vertice.edges[vert]
        return all_edges

    # def path(self, end, start, all, lyst=[]):
    #     if
    #
    # def find_path(self, dest, short_paths, all_edges):
    #     start = ""
    #     temp_path = [dest]
    #     all_paths = []
    #     edge_letters = all_edges.keys()
    #     if short_paths[dest] == math.inf:
    #         return []
    #     for key in short_paths.keys():
    #         if short_paths[key] == 0:
    #             start = key






    def find_all_shortest(self, start):
        """Helper function"""
        for v in self.vertices.values():
            v.dist = math.inf
            v.visited = False
        self.vertices[start].distance = 0
        while False in [x.visited for x in self.vertices.values()]:
            current_searchable = []
            for vertex in self.vertices.values():
                if not vertex.visited:
                    current_searchable.append(vertex)
            distances = [x.distance for x in current_searchable]
            for vertex in current_searchable:
                if vertex.distance == min(distances):
                    node_to_visit = vertex
                    node_to_visit.visited = True
                    adjacent = node_to_visit.get_neighbors()
                    for neighbor in adjacent:
                        if (node_to_visit.distance + node_to_visit.edges[neighbor]) < neighbor.distance:
                            neighbor.distance = node_to_visit.distance + node_to_visit.edges[neighbor]
        labels = [x.label for x in self.vertices.values()]
        distances = [x.distance for x in self.vertices.values()]
        return dict(zip(labels, distances))

    def dijkstra_shortest_path(self, src, dest=None):
        """Shortest path algorithm"""
        all_paths = self.find_all_shortest(src)
        all_edges = self.get_all_edges()
        keys = all_paths.keys()
        values = all_paths.values()
        no_dest = {}
        # if dest:
        #     return (all_paths[dest], self.find_path(dest, all_paths, all_edges))
        # else:
        #     for key in keys:
        #         no_dest[key] = (all_paths[key], self.find_path(key, all_paths, all_edges))
        return all_paths




    def __str__(self):
        """String function"""
        returned_string = ""
        returned_string += f"numVertices: {len(self.vertices.keys())}\n"
        returned_string += "VERTICE   NEIGHBORS\n"
        for vertice in self.vertices.keys():
            neighbor_labels = self.vertices[vertice].edges.keys()
            neighbor_labels_decoded = []
            for item in neighbor_labels:
                neighbor_labels_decoded.append(item.label)
            neighbor_lengths = self.vertices[vertice].edges.values()
            all_neighbor_info = dict(zip(neighbor_labels_decoded, neighbor_lengths))
            returned_string += f"{vertice}   {all_neighbor_info}\n"
        return returned_string


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
# g.add_edge("A", "B", 1.0)
# g.add_edge("A", "C", 1.0)
#
# g.add_edge("B", "D", 1.0)
#
# g.add_edge("C", "E", 1.0)
#
# g.add_edge("E", "F", 1.0)
print(g.dijkstra_shortest_path("A"))
print(g.get_all_edges())
