import networkx as nx
import matplotlib.pyplot as plt

# Створення пустого орієнтованого графа
G = nx.DiGraph()

# Додавання вузлів
G.add_node("A")
G.add_node("B")
G.add_node("C")

# Додавання спрямованих ребер
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("C", "A")

# Малювання графу
nx.draw(
    G,
    with_labels=True,
    node_color="lightblue",
    node_size=1500,
    edge_color="black",
    arrows=True,
)
plt.show()
