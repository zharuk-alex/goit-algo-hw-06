import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("A")
G.add_nodes_from(["B", "C", "D"])

G.add_edge("A", "B")
G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D")])

num_nodes = G.number_of_nodes()  # 4
num_edges = G.number_of_edges()  # 4
is_connected = nx.is_connected(G)  # True

"""
визначається як кількість з'єднань, які має вузол. 
Чим більше з'єднань має вузол, тим більш центральним він є. 
У ненаправлених графах це просто кількість сусідів вузла. 
У направлених графах можна розглядати вхідний і вихідний ступені окремо
"""
degree_centrality = nx.degree_centrality(G)
print(
    degree_centrality
)  # {'A': 0.6666666666666666, 'B': 1.0, 'C': 0.6666666666666666, 'D': 0.3333333333333333}

"""
визначається як обернене значення середньої відстані від вузла до всіх інших вузлів у графі. 
Вузли, які знаходяться ближче до інших вузлів, мають вищу центральність близькості.
"""
closeness_centrality = nx.closeness_centrality(G)
print(closeness_centrality)  # {'A': 0.75, 'B': 1.0, 'C': 0.75, 'D': 0.6}

"""
визначається як кількість найкоротших шляхів між усіма парами вузлів, які проходять через даний вузол.
Ця метрика відображає, наскільки вузол є "мостом" між іншими вузлами у графі.
"""
betweenness_centrality = nx.betweenness_centrality(G)
print(betweenness_centrality)  # {'A': 0.0, 'B': 0.6666666666666666, 'C': 0.0, 'D': 0.0}


"""
найкоротший шлях між двома вузлами або розрахувати середню довжину шляху у графі
"""
path = nx.shortest_path(G, source="A", target="D")  # ['A', 'B', 'D']
avg_path_length = nx.average_shortest_path_length(G)  # 1.3333333333333333


"""circular_layout"""
# G = nx.complete_graph(8)
# pos = nx.circular_layout(G)
# nx.draw(G, pos, with_labels=True)
# plt.title("Circular Layout")
# plt.show()

"""random_layout"""
# G = nx.complete_graph(8)
# pos = nx.random_layout(G)
# nx.draw(G, pos, with_labels=True)
# plt.title("Random Layout")
# plt.show()

"""shell_layout"""
G = nx.complete_graph(8)
pos = [[0, 1, 2], [3, 4], [5, 6, 7]]  # Вказує камери для розташування вершин
pos = nx.shell_layout(G, pos)
nx.draw(G, pos, with_labels=True)
plt.title("Shell Layout")
plt.show()
