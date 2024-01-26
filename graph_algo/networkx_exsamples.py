import networkx as nx
import matplotlib.pyplot as plt

# Створення пустого графу
G = nx.Graph()

# Додавання вузлів
G.add_node("A")
G.add_nodes_from(["B", "C", "D"])


# Додавання ребер
G.add_edge("A", "B")
G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D")])

# Всі вершини
print(G.nodes())
# Всі ребра
print(G.edges())

print(list(G.neighbors("A")))  # ['B', 'C']

# Малювання графу
nx.draw(G, with_labels=True, node_color="skyblue", node_size=1500, edge_color="black")
plt.show()


# G.remove_node("A")
# G.remove_nodes_from(["B", "C"])
# G.remove_edge("A", "B")
# G.remove_edges_from([("A", "C"), ("B", "D")])
