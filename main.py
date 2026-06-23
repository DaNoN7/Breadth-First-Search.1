"""
Пошук у ширину (Breadth-First Search, BFS)
-------------------------------------------
Реалізація алгоритму BFS на графі, представленому списком суміжності.

Містить:
    - bfs()                -> обхід графа, порядок відвідування вершин
    - print_levels()       -> вершини, згруповані по рівнях (відстані від старту)
    - bfs_shortest_path()  -> найкоротший шлях між двома вершинами
"""

from collections import deque


def bfs(graph, start):
    """
    Виконує пошук у ширину (BFS) для графа `graph`, починаючи з вершини `start`.

    :param graph: словник суміжності {вершина: [список_сусідів]}
    :param start: вершина, з якої починається обхід
    :return: список вершин у порядку їх відвідування
    """
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def print_levels(graph, start):
    """
    Виводить вершини графа по рівнях — групами за відстанню
    (у кількості ребер) від вершини `start`.
    """
    visited = {start}
    queue = deque([(start, 0)])
    levels = {}

    while queue:
        vertex, level = queue.popleft()
        levels.setdefault(level, []).append(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))

    for level, vertices in levels.items():
        print(f"  Рівень {level}: {vertices}")


def bfs_shortest_path(graph, start, goal):
    """
    Знаходить найкоротший шлях (за кількістю ребер) між `start` і `goal`
    у незваженому графі за допомогою BFS.

    :return: список вершин шляху, або None, якщо шляху не існує
    """
    if start == goal:
        return [start]

    visited = {start}
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        vertex = path[-1]

        for neighbor in graph.get(vertex, []):
            if neighbor == goal:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None


if __name__ == "__main__":
    # Граф представлений списком суміжності (неорієнтований, незважений)
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    print("Граф (список суміжності):")
    for vertex, neighbors in graph.items():
        print(f"  {vertex}: {neighbors}")

    print("\n--- BFS-обхід з вершини A ---")
    order = bfs(graph, "A")
    print("Порядок відвідування:", order)

    print("\n--- Обхід по рівнях (від A) ---")
    print_levels(graph, "A")

    print("\n--- Найкоротший шлях A -> F ---")
    path = bfs_shortest_path(graph, "A", "F")
    print("Шлях:", path)
