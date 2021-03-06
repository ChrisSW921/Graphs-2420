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


class Graph:
    """Graph class"""
    def __init__(self):
        self.edge_count = 0
        self.vertices = dict()
        self.size = 0
        self.dfs_list = []

    def add_vertex(self, label):
        """Add a vertex to graph"""
        if not (isinstance(label, str)):
            raise ValueError
        self.vertices[label] = Vertex(label)
        self.size += 1
        return self

    def add_edge(self, src, dest, w):
        """Add an edge to graph"""
        if src not in self.vertices.keys() or dest not in self.vertices.keys():
            raise ValueError
        if isinstance(w, str):
            raise ValueError
        src_vertex = self.vertices[src]
        dest_vertex = self.vertices[dest]
        src_vertex.addEdgeTo(dest_vertex, w)
        self.edge_count += 1
        return self

    def get_weight(self, src, dest):
        """Return weight of edge"""
        if src not in self.vertices.keys() or dest not in self.vertices.keys():
            raise ValueError
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
        if starting_vertex not in self.vertices.keys():
            raise ValueError
        starting_vertex = self.vertices[starting_vertex]
        for vertice in self.vertices.values():
            vertice.visited = False
        self.dfs_list = []
        self.dfs_helper(starting_vertex)
        return self.dfs_list

    def dfs(self, starting_vertex):
        """dfs"""
        if starting_vertex not in self.vertices.keys():
            raise ValueError
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
        if src not in self.vertices.keys():
            raise ValueError
        all_paths = self.find_all_shortest(src)
        all_edges = self.get_all_edges()
        no_dest = {}

        coded = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}

        matrix = [[0.0 for x in range(len(self.vertices))] for x in range(len(self.vertices))]

        for item in list(all_edges.keys()):
            matrix[coded[item[0]]][coded[item[1]]] = all_edges[item]

        if dest:
            letter_path = self.dij(coded[src], matrix, all_paths, dest)
            return (all_paths[dest], letter_path)
        else:
            for item in self.vertices.keys():
                if all_paths[item] in [0, math.inf]:
                    no_dest[item] = (all_paths[item], [])
                else:
                    no_dest[item] = (all_paths[item], self.dij(coded[src], matrix, all_paths, item))
            return no_dest

    def clean(self, lyst, dest):
        """Clean function"""
        coded = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}
        desti = coded[dest]
        cleaned = []
        for item in lyst:
            if item[-1] == desti:
                cleaned.append(item)
        return cleaned

    def letter_path(self, lyst, dest, low_num):
        """Convert to letters"""
        back_coded = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F"}
        edges = self.get_all_edges()
        for path in lyst:
            count = 0
            i = 0
            j = 1
            for x in path[:-1]:
                count += edges[(back_coded[path[i]], back_coded[path[j]])]
                i += 1
                j += 1
            if count == low_num:
                letters = [back_coded[x] for x in path]
                letters.reverse()
                return letters

    def dij(self, src, matrix, all_paths, dest):
        """Helper function"""
        paths = []
        for item in matrix[src]:
            if item > 0:
                paths.append([src, matrix[src].index(item)])
        rough =[]
        for item in self.recurse(matrix, paths):
            rough.append(item)
        all_possible_paths = self.clean(rough, dest)
        letters = self.letter_path(all_possible_paths, dest, all_paths[dest])
        return letters

    def recurse(self, matrix, paths, check=[]):
        """Helper function"""
        temp_paths = []
        check_paths = []
        continues = False

        for item in check:
            temp_paths.append(item)
        for item in paths:
            temp_paths.append(item)

        for item in paths:
            for x in matrix[item[-1]]:
                if x > 0:
                    temp_list = item.copy()
                    temp_list.append(matrix[item[-1]].index(x))
                    check_paths.append(temp_list)
                    continues = True
        if continues:
            return self.recurse(matrix, check_paths, temp_paths)
        else:
            return temp_paths

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
