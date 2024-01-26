# dfs bfs
from collections import deque
from pages_graph import links
from graph_algo.bfs import bfs_iterative, bfs_recursive
from graph_algo.dfs import dfs_iterative, dfs_recursive

target = "top_product"
links_dict = {}
for source, target, _ in links:
    if source not in links_dict:
        links_dict[source] = []
    links_dict[source].append(target)


print("bfs_recursive: ")
bfs_recursive(links_dict, deque([target]))
print("\n\ndfs_recursive: ")
dfs_recursive(links_dict, target)

# bfs_iterative(links_dict, target)
# dfs_iterative(links_dict, target)
