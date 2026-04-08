from graph import Graph
import tkinter as tk 
import math

class GraphVisualiser(tk.Tk): 
    def __init__(self, graph):
        super().__init__()
        self.title("Graph Visualiser") # s not z - British English
        self.graph = graph

        self.canvas = tk.Canvas(self, width=400, height=400, bg='white')
        self.canvas.pack()
        self.vertex_positions = {}
        self.draw_graph()

        control_frame = tk.Frame(self)
        control_frame.pack()

        tk.Label(control_frame, text="Vertices:").grid(row=0, column=0)
        self.vertices_entry = tk.Entry(control_frame, width=10)
        self.vertices_entry.grid(row=0, column=1)

        add_vertice_btn = tk.Button(control_frame, text="Add vertice", command=self.add_vertex)
        add_vertice_btn.grid(row=0, column=2)
        remove_vertice_btn = tk.Button(control_frame, text="Remove vertice", command=self.remove_vertex)
        remove_vertice_btn.grid(row=0, column=3)

        tk.Label(control_frame, text="Edges:").grid(row=2, column=0)
        self.edge_entry = tk.Entry(control_frame, width=10)
        self.edge_entry.grid(row=2, column=1)

        add_edge_btn = tk.Button(control_frame, text="Add edge", command=self.add_edge)
        add_edge_btn.grid(row=2, column=2)
        remove_edge_btn = tk.Button(control_frame, text="Remove edge", command=self.remove_edge)
        remove_edge_btn.grid(row=2, column=3)


    
    def draw_graph(self):
        self.canvas.delete("all")
        radius = 20
        spacing = 100
        # Arrange vertices in a circle  
        n = len(self.graph.graph)
        angle_gap = 360 / n if n else 0
        center_x, center_y = 200, 200
        for i, v in enumerate(self.graph.graph):
            angle = i * angle_gap
            x = center_x + spacing * math.cos(math.radians(angle)) # Error with tk.math - so imported math instead
            y = center_y + spacing * math.sin(math.radians(angle))
            self.vertex_positions[v] = (x, y)
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='lightblue')
            self.canvas.create_text(x, y, text=v)
        
        # Draw edges
        for v in self.graph.graph:
            x1, y1 = self.vertex_positions[v]
            for nbr in self.graph.graph[v]:
                x2, y2 = self.vertex_positions[nbr]
                self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST if self.graph.directed else None)
                if self.graph.weighted:
                    w = self.graph.weights.get((v, nbr), '')
                    mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
                    self.canvas.create_text(mid_x, mid_y, text=str(w), fill="red")

    def add_vertex(self):
        vertex = self.vertices_entry.get()
        if not vertex:
            return
        
        self.graph.add_vertex(vertex)
        self.vertices_entry.delete(0, tk.END)
        self.draw_graph()


    def remove_vertex(self, vertex): #Not altered to fit visualiser
        if vertex in self.graph:
            del self.graph[vertex] # Remove the vertex from the graph
            # Remove all edges associated with the vertex
            for v in self.graph:
                if vertex in self.graph[v]:
                    self.graph[v].remove(vertex)
                    if self.weighted:
                        del self.weights[(v, vertex)]
                        if not self.directed:
                            del self.weights[(vertex, v)]
        else:
            print("Vertex not found in graph.")


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


    

if __name__ == "__main__":
    g = Graph(directed=True, weighted=True)
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_edge('A', 'B', 10)
    g.add_edge('B', 'C', 20)
    g.add_edge('C', 'A', 30)

    app = GraphVisualiser(g)
    app.mainloop()
