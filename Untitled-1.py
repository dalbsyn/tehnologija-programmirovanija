def dijkstra(graph, start, end):
    # Словарь для хранения кратчайших путей и их стоимости
    shortest_paths = {start: (None, 0)}
    visited = set()

    while True:
        # Находим ближайший узел, который ещё не посещён
        current_node = None
        for node in shortest_paths:
            if node not in visited and (current_node is None or shortest_paths[node][1] < shortest_paths[current_node][1]):
                current_node = node

        if current_node is None:  # Если нет доступных узлов
            return "Маршрут не существует"
        if current_node == end:  # Если достигли конечного узла
            break

        visited.add(current_node)
        current_weight = shortest_paths[current_node][1]

        # Обновляем веса соседей текущего узла
        for neighbor, weight in graph[current_node].items():
            new_weight = current_weight + weight
            if neighbor not in shortest_paths or new_weight < shortest_paths[neighbor][1]:
                shortest_paths[neighbor] = (current_node, new_weight)

    # Восстанавливаем путь
    path = []
    while current_node is not None:
        path.append(current_node)
        current_node = shortest_paths[current_node][0]
    return path[::-1]


graph = {
    "Чкаловская": {"Адмиралтейская": 15},
    "Адмиралтейская": {"Чкаловская": 15, "Невский проспект": 8, "Сенная площадь": 10},
    "Невский проспект": {"Адмиралтейская": 8, "Сенная площадь": 7, "Московский вокзал": 12},
    "Сенная площадь": {"Адмиралтейская": 10, "Невский проспект": 7, "Владимирская": 14, "Технологический институт": 5},
    "Технологический институт": {"Сенная площадь": 5, "Владимирская": 8},
    "Владимирская": {"Сенная площадь": 14, "Технологический институт": 8, "Московский вокзал": 6, "Пл. Александра Невского": 8},
    "Московский вокзал": {"Невский проспект": 12, "Владимирская": 6, "Пл. Александра Невского": 12, "Девяткино": 18},
    "Девяткино": {"Московский вокзал": 18},
    "Пл. Александра Невского": {"Владимирская": 8, "Московский вокзал": 12, "Ладожская": 8},
    "Ладожская": {"Пл. Александра Невского": 8}
}

print("Путь из Девяткино на Ладожскую:", dijkstra(graph, "Девяткино", "Ладожская"))
print("Путь из Чкаловская на Ладожская:", dijkstra(graph, "Чкаловская", "Ладожская"))

