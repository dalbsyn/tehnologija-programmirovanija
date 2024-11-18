import matplotlib.pyplot as plt

# Данные
x = list(range(1, len(resistance_R2) + 1))  # Индексы для оси X
resistance_R2 = [38.6, 39.1, 41.5, 43.1, 41.9, 40.4, 37.9, 37.4, 37.7, 38.2, 38.7, 39.3, 39.7, 40.3, 40.7, 41.2, 41.6, 42.0, 42.5, 43.0, 43.4]
resistance_R1 = [2.30, 1.83, 1.71, 1.47, 1.26, 1.07, 0.90, 0.60, 0.72, 0.61, 0.53, 0.46, 0.40, 0.34, 0.28, 0.25, 0.21, 0.17, 0.14, 0.11, 0.09]

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(x, resistance_R2, marker='o', label='R2 (Ω)')
plt.plot(x, resistance_R1, marker='s', label='R1 (Ω)')
plt.xlabel('Номер измерения')
plt.ylabel('Сопротивление (Ω)')
plt.title('График сопротивлений R1 и R2')
plt.legend()
plt.grid(True)
plt.show()
