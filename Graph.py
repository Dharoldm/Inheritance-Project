import random
import copy


class Graph(object):
    class Edge(object):
        def __init__(self, source, destination, weight):
            """
            DO NOT EDIT!
            Class representing an Edge in a graph
            :param source: Vertex where this edge originates
            :param destination: Vertex where this edge ends
            :param weight: Value associated with this edge
            """
            self.source = source
            self.destination = destination
            self.weight = weight

        def __eq__(self, other):
            return self.source == other.source and self.destination == other.destination

        def __repr__(self):
            return f"Source: {self.source} Destination: {self.destination} Weight: {self.weight}"

        __str__ = __repr__

    class Path(object):
        def __init__(self, vertices=list(), weight=0):
            """
            DO NOT EDIT!
            Class representing a path in a graph
            :param vertices: Ordered list of vertices that compose the path
            :param weight: Total weight of the path
            """
            self.vertices = vertices
            self.weight = weight

        def __eq__(self, other):
            return self.vertices == other.vertices and self.weight == other.weight

        def __repr__(self):
            return f"Weight:{self.weight} Path: {' -> '.join([str(v) for v in self.vertices])}\n"

        __str__ = __repr__

        def add_vertex(self, vertex):
            """
            Add a vertex id to the path
            :param vertex: id of a vertex
            :return: None
            """
            self.vertices.append(vertex)

        def add_weight(self, weight):
            """
            Add weight to the path
            :param weight: weight
            :return: None
            """
            self.weight += weight

        def remove_vertex(self):
            """

            Remove the most recently added vertex from the path
            :return: None
            """
            if not self.is_empty():
                self.vertices.pop()

        def is_empty(self):
            """
            Check if the path object is empty
            :return: True if empty, False otherwise
            """
            return len(self.vertices) == 0

    class Vertex(object):
        def __init__(self, number):
            """
            Class representing a vertex in the graph
            :param number: Unique id of this vertex
            """
            self.edges = []
            self.id = number
            self.visited = False

        def __repr__(self):
            return f"Vertex: {self.id}"

        __str__ = __repr__

        def add_edge(self, destination, weight):
            """
            Adds an edge to the Vertex
            :param destination: The id of the destination Vertex
            :param weight: The weight of the edge being added
            :return: None
            """
            self.edges.append(Graph.Edge(self, destination, weight))

        def degree(self):
            """
            Returns the number of edges on the vertex
            :return: The degree of the vertex
            """
            degree = 0
            for i in self.edges:
                degree += 1
            return degree

        def get_edge(self, destination):
            """
            Gets the edge object to the specified destination
            :param destination: The id of the destination of the desired edge
            :return: If the edge is found, the edge object. If the edge isn't found, None
            """
            for i in self.edges:
                if i.destination == destination:
                    return i
            return None

        def get_edges(self):
            """
            :return: A list of the edges of the vertex
            """
            return self.edges


    def __init__(self, size=0, connectedness=0):
        """
        DO NOT EDIT THIS METHOD
        Construct a random DAG
        :param size: Number of vertices
        :param connectedness: Value from 0 - 1 with 1 being a fully connected graph
        """
        assert connectedness <= 1
        self.adj_map = {}
        self.size = size
        self.connectedness = connectedness
        self.construct_graph()

    def construct_graph(self):
        """
        Creates vertices and edges within the graph using the result of generate_edges
        :return: None
        """
        edges_list = []
        for i in edges_list:
            if i[0] not in self.adj_map:      # check if the source Vertex exists
                source = Graph.Vertex(i[0])
                self.adj_map[source.id] = source
            if i[1] not in self.adj_map:      # check if the destination Vertex exists
                destination = Graph.Vertex(i[1])
                self.adj_map[destination.id] = destination
            source = self.adj_map[i[0]].id
            destination = self.adj_map[i[1]].id
            self.insert_edge(source, destination, i[2])
        return

    def vertex_count(self):
        """
        :return: The number of vertices in the graph
        """
        return self.size

    def vertices(self):
        """
        :return: A list of all vertices within the graph
        """
        return_list = []
        for i in self.adj_map:
            return_list.append(self.adj_map[i])
        return return_list

    def insert_edge(self, source, destination, weight):
        """
        Creates an edge for the given vertex with the given destination and weight
        :param source: The id of the source vertex
        :param destination: The id of the destination vertex
        :param weight: The weight of the edge
        :return: None
        """
        for i in self.adj_map[source].edges:
            if i.destination == destination:
                i.weight = weight
        self.adj_map[source].add_edge(destination, weight)

    def find_valid_paths(self, source, destination, limit):
        """
        Finds all valid paths between source and destination with a weight less than or equal to the given limit
        :param source: The id of the source vertex
        :param destination: The id of the destination vertex
        :param limit: The weight limit
        :return: A list of all valid paths
        """
        # If any of the inputs are not ints return an empty list
        if not isinstance(source, int) or not isinstance(destination, int) or not isinstance(limit, int):
            return []
        # If either source or destination are not in the map then return an empty list
        if source not in self.adj_map:
            return []
        if destination not in self.adj_map:
            return []
        valid = []                  # The return list of all valid paths
        visited = list()  # List of vertexes visited
        Graph.find_valid_paths_recurr(self, source, destination, limit, visited, valid)  # Call the recursive function
        for i in self.adj_map:
            self.adj_map[i].visited = False     # Mark all vertices as unvisited again so the function can be used again
        return valid

    def find_valid_paths_recurr(self, source, destination, limit, visited, valid, weight=0):
        """
        Looks to see if the given vertex is equal to destination. If it does then it creates a path with the given
        list of visited vertices and current weight of all edges. If it doesn't It calls itself with again using all
        vertices the vertex has an edge with and then returns the list of valid paths.
        :param source: The id of the current vertex
        :param destination: The id of the destination vertex
        :param limit: The limit on the weight
        :param visited: A list of all vertices in the current path
        :param valid: A list of all valid paths
        :param weight: The total weight of the current path
        :return: Valid, the list of all valid paths
        """
        visited.append(source)
        # If the vertex is marked visited, then it will not lead to the destination
        if self.adj_map[source].visited is True:
            return valid
        self.adj_map[source].visited = True
        if source == destination:
            # Mark all the vertices in the current path as unvisited as they can lead to the destination
            for i in visited:
                self.adj_map[i].visited = False
            if weight <= limit:
                # Create a new path with the current visited list and add it to the valid path list
                valid_path = copy.deepcopy(Graph.Path(visited, weight))
                valid.append(valid_path)
            return valid
        # Check if the source has any edges, if it doesn't return valid
        if len(self.adj_map[source].edges) == 0:
            return valid
        # Recursively call the function using every edge the current vertex has
        for i in self.adj_map[source].edges:
            weight += i.weight # Add the edge's weight to the total weight
            Graph.find_valid_paths_recurr(self, i.destination, destination, limit, visited, valid, weight)
            visited.pop()  # Remove the last visited vertex from the visited list
            weight -= i.weight  # Remove the edge's weight the to total weight
        return valid  # Return the list of total valid paths

    def find_shortest_path(self, source, destination, limit):
        """
        Creates a list of all valid paths and returns the path with the smallest weight
        :param source:  The id of the source vertex
        :param destination:  The id of the destination vertex
        :param limit:  The limit of the weight of the path
        :return:  The path with the least weight
        """
        paths = Graph.find_valid_paths(self, source, destination, limit)
        if len(paths) == 0:
            return []
        least = paths[0]
        for i in paths:
            if i.weight < least.weight:
                least = i
        return least

    def find_longest_path(self, source, destination, limit):
        """
        Creates a list of all valid paths and returns the path with the largest weight
        :param source:  The id of the source vertex
        :param destination:  The id of the destination vertex
        :param limit:  The limit of the weight of the path
        :return:  The path with the largest weight
        """
        paths = Graph.find_valid_paths(self, source, destination, limit)
        if len(paths) == 0:
            return []
        longest = paths[0]
        for i in paths:
            if i.weight > longest.weight:
                longest = i
        return longest

    def find_most_vertices_path(self, source, destination, limit):
        """
        Creates a list of all valid paths and returns the path with the most vertices
        :param source:  The id of the source vertex
        :param destination:  The id of the destination vertex
        :param limit:  The limit of the weight of the path
        :return:  The path with the most vertices
        """
        paths = Graph.find_valid_paths(self, source, destination, limit)
        if len(paths) == 0:
            return []
        most = paths[0]
        for i in paths:
            if len(i.vertices) > len(most.vertices):
                most = i
        return most

    def find_least_vertices_path(self, source, destination, limit):
        """
        Creates a list of all valid paths and returns the path with the least vertices
        :param source:  The id of the source vertex
        :param destination:  The id of the destination vertex
        :param limit:  The limit of the weight of the path
        :return:  The path with the least vertices
        """
        paths = Graph.find_valid_paths(self, source, destination, limit)
        if len(paths) == 0:
            return []
        shortest = paths[0]
        for i in paths:
            if len(i.vertices) < len(shortest.vertices):
                shortest = i
        return shortest
