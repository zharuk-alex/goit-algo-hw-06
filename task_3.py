import networkx as nx
from pages_graph import G

# dijkstra

shortest_path = nx.shortest_path(
    G, source="top_product", target="index", weight="weight"
)

shortest_path_dijkstra = nx.single_source_dijkstra_path(
    G, source="top_product", weight="weight"
)

shortest_path_target_index = shortest_path_dijkstra.get("index")
# print(
#     "shortest_path_dijkstra | top_product | index | ", shortest_path_target_index, "\n"
# )

shortest_path_dijkstra_len = nx.single_source_dijkstra_path_length(
    G, "top_product", cutoff=None, weight="weight"
)


# print(shortest_path_dijkstra_len)
# print("method name | source | target | result\n")
print("shortest_path | top_product | index | ", shortest_path, "\n")
