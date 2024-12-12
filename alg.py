import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt
import time

# Создание основного окна
root = tk.Tk()
root.title("Алгоритмы поиска кратчайшего пути")
root.geometry("800x600")

# Глобальная переменная для графа
graph = nx.DiGraph()

# Функция для добавления ребра в граф
def add_edge():
    try:
        src = source_entry.get()
        dest = dest_entry.get()
        weight = int(weight_entry.get())
        graph.add_edge(src, dest, weight=weight)
        messagebox.showinfo("Успех", f"Добавлено ребро: {src} -> {dest} с весом {weight}")
    except ValueError:
        messagebox.showerror("Ошибка", "Вес должен быть числом")

# Функция для удаления ребра из графа
def delete_edge():
    try:
        src = source_entry.get()
        dest = dest_entry.get()
        if graph.has_edge(src, dest):
            graph.remove_edge(src, dest)
            messagebox.showinfo("Успех", f"Удалено ребро: {src} -> {dest}")
        else:
            messagebox.showerror("Ошибка", "Ребро не существует")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось удалить ребро: {e}")

# Функция для отображения графа
def draw_graph():
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()

# Функция для нахождения кратчайшего пути

def find_shortest_path(algorithm):
    try:
        start_node = start_entry.get()
        end_node = end_entry.get()
        if algorithm == 'A*':
            heuristic = {node: 1 for node in graph.nodes}  # Простая эвристика
            start_time = time.time()
            path = nx.astar_path(graph, start_node, end_node, heuristic=heuristic.get)
            exec_time = time.time() - start_time
        elif algorithm == 'Dijkstra':
            start_time = time.time()
            path = nx.dijkstra_path(graph, start_node, end_node)
            exec_time = time.time() - start_time
        elif algorithm == 'DFS':
            start_time = time.time()
            path = list(nx.dfs_edges(graph, source=start_node))
            exec_time = time.time() - start_time
            path = [start_node] + [edge[1] for edge in path if edge[0] != edge[1]]
        else:
            raise ValueError("Неизвестный алгоритм")

        messagebox.showinfo("Результат", f"Алгоритм: {algorithm}\nПуть: {' -> '.join(path)}\nВремя выполнения: {exec_time:.6f} секунд")
    except nx.NetworkXNoPath:
        messagebox.showerror("Ошибка", "Путь между указанными узлами не найден")
    except nx.NodeNotFound:
        messagebox.showerror("Ошибка", "Указанные узлы отсутствуют в графе")

# UI элементы
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

source_label = tk.Label(frame_top, text="Источник:")
source_label.grid(row=0, column=0, padx=5, pady=5)
source_entry = tk.Entry(frame_top)
source_entry.grid(row=0, column=1, padx=5, pady=5)

dest_label = tk.Label(frame_top, text="Назначение:")
dest_label.grid(row=1, column=0, padx=5, pady=5)
dest_entry = tk.Entry(frame_top)
dest_entry.grid(row=1, column=1, padx=5, pady=5)

weight_label = tk.Label(frame_top, text="Вес:")
weight_label.grid(row=2, column=0, padx=5, pady=5)
weight_entry = tk.Entry(frame_top)
weight_entry.grid(row=2, column=1, padx=5, pady=5)

add_edge_button = tk.Button(frame_top, text="Добавить ребро", command=add_edge)
add_edge_button.grid(row=3, columnspan=2, pady=5)

delete_edge_button = tk.Button(frame_top, text="Удалить ребро", command=delete_edge)
delete_edge_button.grid(row=4, columnspan=2, pady=5)

draw_graph_button = tk.Button(frame_top, text="Показать граф", command=draw_graph)
draw_graph_button.grid(row=5, columnspan=2, pady=5)

frame_bottom = tk.Frame(root)
frame_bottom.pack(pady=10)

start_label = tk.Label(frame_bottom, text="Начальная вершина:")
start_label.grid(row=0, column=0, padx=5, pady=5)
start_entry = tk.Entry(frame_bottom)
start_entry.grid(row=0, column=1, padx=5, pady=5)

end_label = tk.Label(frame_bottom, text="Конечная вершина:")
end_label.grid(row=1, column=0, padx=5, pady=5)
end_entry = tk.Entry(frame_bottom)
end_entry.grid(row=1, column=1, padx=5, pady=5)

algorithm_frame = tk.Frame(root)
algorithm_frame.pack(pady=10)

a_star_button = tk.Button(algorithm_frame, text="Запуск A*", command=lambda: find_shortest_path('A*'))
a_star_button.grid(row=0, column=0, padx=10, pady=5)

dijkstra_button = tk.Button(algorithm_frame, text="Запуск Дейкстры", command=lambda: find_shortest_path('Dijkstra'))
dijkstra_button.grid(row=0, column=1, padx=10, pady=5)

dfs_button = tk.Button(algorithm_frame, text="Запуск DFS", command=lambda: find_shortest_path('DFS'))
dfs_button.grid(row=0, column=2, padx=10, pady=5)

root.mainloop()
