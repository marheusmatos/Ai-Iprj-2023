import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout

# List of edges (example)
edges = [(1, 2), (2, 3), (2, 4), (4, 5)]

# Create an empty directed graph
graph = nx.DiGraph()

# Add edges from the list
graph.add_edges_from(edges)

# Generate the layout using graphviz_layout with "dot" program
pos = graphviz_layout(graph, prog="dot")

# Draw the graph as a tree
nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=800, font_weight='bold')

# Display the graph
plt.show()



def dfs_recursiva(grafo, vertice, visitados):
    visitados.add(vertice)
    for vizinho in grafo[vertice]:
        if vizinho not in visitados:
            dfs_recursiva(grafo, vizinho, visitados)

