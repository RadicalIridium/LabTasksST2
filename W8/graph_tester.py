# === graph_tester.py === #
from graph import Graph

#Basic undirected graph tests
"""
print("Undirected Graph:")
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.print_graph()
print()

g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.print_graph()
print()

g.remove_edge('B', 'C')
g.print_graph()
print("-" *10)


# Directed graph tests
print("Directed Graph:")
g = Graph(directed=True)
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.print_graph()
print()

g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.print_graph()
print()

g.remove_edge('B', 'C')
g.print_graph()
print("-" *10)

# Weighted graph tests

print("Weighted Directed Graph:")
g = Graph(weighted=True, directed=True)
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.print_graph()
print()

g.add_edge('A', 'B', 15)
g.add_edge('B', 'C', 34)
g.add_edge('C', 'D', 7)
g.print_graph()
print()

g.remove_edge('B', 'C')
g.print_graph()
print("-" *10)
"""
"""
print("Undirected Graph:") #Graph for BFS and DFS testing
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.print_graph()
"""

# BFS on the graph from Activity 1 -Task2
"""
print("BFS starting from vertex 'A':")
visited_bfs = list(g.bfs('A'))
print("Visited vertices in BFS order:", visited_bfs)
"""
"""
# DFS on the same graph
print("DFS starting from vertex 'A':")
visited_dfs = list(g.dfs('A')) #added list() 
print("Visited vertices in DFS order:", visited_dfs)
"""

"""
# Task 4: Cycle Detection
#cycle detection in undirected graphs
# Create graph with a cycle
cycle_graph = Graph(directed=False)
for v in ['A', 'B', 'C']:
    cycle_graph.add_vertex(v)
cycle_graph.add_edge('A', 'B')
cycle_graph.add_edge('B', 'C')
cycle_graph.add_edge('C', 'A') # Closing the cycle

print("Does cycle_graph have a cycle? ", cycle_graph.has_undirected_cycle())

# Create graph without a cycle
acyclic_graph = Graph(directed=False)
for v in ['X', 'Y', 'Z']:
    acyclic_graph.add_vertex(v)
acyclic_graph.add_edge('X', 'Y')
acyclic_graph.add_edge('Y', 'Z')
print("Does acyclic_graph have a cycle? ",
acyclic_graph.has_undirected_cycle())
"""

#Task 5: Experiment with Weighted and Directed Graphs
# Create weighted directed graph
wg = Graph(directed=True, weighted=True)
for v in ['A', 'B', 'C']:
    wg.add_vertex(v)
wg.add_edge('A', 'B', weight=15)
wg.add_edge('B', 'C', weight=34)
wg.add_edge('A', 'C', weight=50)
print("Weighted Directed Graph:")
wg.print_graph()



