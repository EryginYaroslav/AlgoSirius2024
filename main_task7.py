class Graph:
    def __init__(self):
        # Список рёбер: (u, v, вес)
        self.edges = []
        self.vertices = set()

    def add_edge(self, u, v, weight):
        """Добавляет направленное ребро с весом между вершинами u и v."""
        self.edges.append((u, v, weight))
        self.vertices.update([u, v])

    def execute_bford_algorythm(self, source):
        """Упрощённая версия алгоритма Беллмана-Форда."""
        # Инициализация расстояний
        dist = {vertex: float('inf') for vertex in self.vertices}
        dist[source] = 0

        # Релаксация рёбер |V|-1 раз
        for _ in range(len(self.vertices) - 1):
            updated = False
            for u, v, weight in self.edges:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    updated = True
            if not updated:  # Если ничего не обновилось, можно прервать
                break

        # Проверка на отрицательный цикл
        for u, v, weight in self.edges:
            if dist[u] + weight < dist[v]:
                return None  # Найден отрицательный цикл

        return dist

if __name__ == '__main__':
    # Создаём граф и добавляем рёбра
    cities_graph = Graph()
    cities_graph.add_edge('Москва', 'Санкт-Петербург', 7)
    cities_graph.add_edge('Санкт-Петербург', 'Выборг', 3)
    cities_graph.add_edge('Выборг', 'Рускеала', 4)
    cities_graph.add_edge('Рускеала', 'Москва', 10)

    # Выполнение алгоритма
    source = 'Москва'
    shortest_paths = cities_graph.execute_bford_algorythm(source)

    if shortest_paths:
        print(f\"Кратчайшие пути от '{source}': {shortest_paths}\")
    else:
        print(\"Обнаружен отрицательный цикл в графе. Кратчайшие пути не определены.\")
