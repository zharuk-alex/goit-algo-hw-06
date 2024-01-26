import random

# Кількість вершин
N = 5

# Створення матриці суміжності розміром 20x20
adj_matrix = [[0 for _ in range(N)] for _ in range(N)]

# Заповнення матриці випадковими значеннями
for i in range(N):
    for j in range(i + 1, N):
        adj_matrix[i][j] = adj_matrix[j][i] = random.randint(0, 1)

# Друк матриці
for row in adj_matrix:
    print(" ".join(map(str, row)))
