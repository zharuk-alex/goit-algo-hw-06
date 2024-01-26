import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

pages = ["index", "ecommerce", "category_1", "product_1", "top_product"]
G.add_nodes_from(pages)

# seo weight
links = [
    ("index", "ecommerce", 6),
    ("ecommerce", "category_1", 3),
    ("category_1", "product_1", 4),
    ("category_1", "index", 2),
    ("ecommerce", "product_1", 5),
    ("product_1", "ecommerce", 3),
    ("category_1", "top_product", 5),
    ("ecommerce", "top_product", 4),
    ("top_product", "ecommerce", 3),
]

G.add_weighted_edges_from(links)
pos = nx.circular_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="skyblue",
    node_size=1000,
    edge_color="black",
    arrows=True,
)

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

if __name__ == "__main__":
    plt.show()
