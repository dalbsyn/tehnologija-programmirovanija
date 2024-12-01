import numpy as np
import matplotlib.pyplot as plt

def is_safe(board, row, col, n):
    if 1 in board[row]:
        return False

    for i in range(n):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def visualize_board(board):
    n = len(board)
    board_colors = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                board_colors[i, j] = 1  # Белые клетки

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(board_colors, cmap="gray", origin="upper")
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                ax.text(j, i, '♛', fontsize=30, ha='center', va='center', color='red')
    
    ax.set_xticks(np.arange(-0.5, n, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, n, 1), minor=True)
    ax.grid(which="minor", color="black", linestyle='-', linewidth=2)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    plt.show()

def check_victory(board):
    n = len(board)
    positions = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                positions.append((i, j))

    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            r1, c1 = positions[i]
            r2, c2 = positions[j]
            if r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
                return False
    return True

def main():
    n = 8
    board = [[0] * n for _ in range(n)]
    queens_count = 0
    
    print("Игра 8 ферзей. Введите координаты для ферзя.")
    print("Координаты в формате: строка колонка (нумерация с 0).")
    print("Например, для верхнего левого угла: 0 0")
    
    while queens_count < 8:
        try:
            visualize_board(board)
            print(f"Вы поставили {queens_count} ферзей. Осталось: {8 - queens_count}.")
            coords = input("Введите координаты: ").strip()
            row, col = map(int, coords.split())
            
            if 0 <= row < n and 0 <= col < n:
                if board[row][col] == 0 and is_safe(board, row, col, n):
                    board[row][col] = 1
                    queens_count += 1
                else:
                    print("Невозможно поставить ферзя в эту клетку! Она под атакой или уже занята.")
                    if not is_safe(board, row, col, n):
                        print("Поражение! Один из ферзей атакует другого.")
                        visualize_board(board)
                        return
            else:
                print("Координаты вне границ доски. Попробуйте снова.")
        except (ValueError, IndexError):
            print("Неверный ввод. Введите два числа через пробел.")

    visualize_board(board)
    
    if check_victory(board):
        print("Поздравляем! Вы выиграли! Все ферзи не атакуют друг друга.")
    else:
        print("К сожалению, вы проиграли. Есть ферзи, которые атакуют друг друга.")

if __name__ == "__main__":
    main()

