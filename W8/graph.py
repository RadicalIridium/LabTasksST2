"""
Code provided by University of Canberra, Class Software Tech 2 2026
"""
#===graph.py===#
from queue import Queue


class Graph:
    def __init__(self, directed=False, weighted=False):
        self.graph = {} # Initialize an empty dictionary to store the adjacency list
        self.weights = {}
        self.directed = directed
        self.weighted = weighted


    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = [] # Add a new vertex with an empty list of edges

    def remove_vertex(self, vertex):
        if vertex not in self.graph:
            return False  # tell GUI vertex was not found

        # Remove edges pointing to this vertex
        for v in self.graph:
            if vertex in self.graph[v]:
                self.graph[v].remove(vertex)
                if self.weighted:
                    self.weights.pop((v, vertex), None)
                    if not self.directed:
                        self.weights.pop((vertex, v), None)

        # Remove the vertex itself
        del self.graph[vertex]

        # Remove any weights involving this vertex
        if self.weighted:
            to_remove = [k for k in self.weights if vertex in k]
            for k in to_remove:
                del self.weights[k]

        return True  # tell GUI removal succeeded


    def add_edge(self, vertex1, vertex2, weight=0):
        if vertex1 in self.graph and vertex2 in self.graph: #Check that vertices are present
    
            # store vertex and weight as a tuple
            self.graph[vertex1].append(vertex2)
            if self.weighted:
                self.weights[(vertex1, vertex2)] = weight
            if not self.directed: # In the case of an undirected graph, append in both directions
                self.graph[vertex2].append(vertex1)
                if self.weighted:
                    self.weights[(vertex2, vertex1)] = weight
        else:
            print("One or both vertices not found in graph.")

    def remove_edge(self, vertex1, vertex2): #provided by autofill - not tested
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2) # Remove the edge from vertex1 to vertex2
                if self.weighted:
                    del self.weights[(vertex1, vertex2)]
            if not self.directed and vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1) # Remove the edge from vertex2 to vertex1
                if self.weighted:
                    del self.weights[(vertex2, vertex1)]
        else:
            print("One or both vertices not found in graph.")

    def print_graph(self): 
        for vertex, edges in self.graph.items():
            if self.weighted:
                edge_info = []
                for edge in edges:
                    weight = self.weights.get((vertex, edge), 0)
                    edge_info.append(f"{edge} (weight: {weight})")
                print(f"{vertex}: {', '.join(edge_info)}")
            else:
                print(f"{vertex}: {', '.join(edges)}")

    def bfs(self, start):
        visited = set()
        queue = []

        queue.append(start)
        visited.add(start)

        while queue:
            vertex = queue.pop(0)
            yield vertex

            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

    def dfs(self, start): #autofill - not tested
        visited = set()
        stack = []

        stack.append(start)
        visited.add(start)

        while stack:
            vertex = stack.pop()
            yield vertex

            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)

    def has_undirected_cycle (self): #autofill - not tested,
        visited = set()

        def dfs(vertex, parent):
            visited.add(vertex)
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    if dfs(neighbour, vertex):
                        return True
                elif neighbour != parent:
                    return True
            return False

        for vertex in self.graph:
            if vertex not in visited:
                if dfs(vertex, None):
                    return True
        return False

    """
    def bfs(self, n): #provide by UNI Canberra, Book Chapter 14 - Graphs.pptx 2026
        #self.validIndex(n)
        visited = [False] *self.nVertices()
        queue = Queue()
        queue.insert(n)
        visited[n] = True
        while not queue.isEmpty():
            visit = queue.remove()
            yield visit
            for j in self.adjacentUnvisitedVertices(visit, visited):
                visited[j] = True
                queue.insert(j)
    """

