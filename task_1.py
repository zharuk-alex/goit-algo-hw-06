import networkx as nx
from pages_graph import G

print("Nodes: ", G.nodes())
print("Total nodes: ", G.number_of_nodes())
print("Total edges: ", G.number_of_edges())

degree_centrality = nx.degree_centrality(G)
max_degree_centrality_node = max(degree_centrality, key=degree_centrality.get)
max_degree_centrality_value = degree_centrality[max_degree_centrality_node]
print(
    "Max degree centrality: ", max_degree_centrality_node, max_degree_centrality_value
)


path = nx.shortest_path(G, source="index", target="top_product", weight="weight")
print("path to top_product:", path)


# print("Closeness centrality: ", nx.closeness_centrality(G))
# print("Betweenness centrality", nx.betweenness_centrality(G))
