from graph import Graph
import tkinter as tk
from tkinter import messagebox 
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


    def remove_vertex(self): #Not altered to fit visualiser
        vertex = self.vertices_entry.get().strip()
        
        if not vertex:
            return
        
        success = self.graph.remove_vertex(vertex)

        if not success:
            messagebox.showerror("Error", "Vertex not found in graph.")
        else:
            self.vertices_entry.delete(0, tk.END)
            self.draw_graph()


    def add_edge(self):
        val = self.edge_entry.get().replace(',', ' ').split()
        
        if len(val) < 2:
            messagebox.showerror("Error", "Please enter an edge in the format 'A-B'.")
            return
        
        v1, v2 = val[0], val[1]

        if len(val) >= 3:
            try:
                weight = int(val[2])
            except ValueError:
                messagebox.showerror("Error", "Invalid weight. Please enter an integer weight after the vertices.")
                return
        else:
            weight = 0

        self.graph.add_edge(v1, v2, weight)
        self.edge_entry.delete(0, tk.END)
        self.draw_graph()

    def remove_edge(self): 
        val = self.edge_entry.get().replace(',', ' ').split()
        if len(val) < 2:
            messagebox.showerror("Error", "Please enter an edge in the format 'A-B'.")
            return
        
        v1, v2 = val[0], val[1]

        self.graph.remove_edge(v1, v2)
        self.edge_entry.delete(0, tk.END)
        self.draw_graph()
    

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
