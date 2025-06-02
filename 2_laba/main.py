import numpy as np
from scipy.optimize import linprog

# Исходная матрица интенсивности
intensity_matrix = {
    "A1": {"S1": 36, "S2": 36, "S3": 36},
    "A2": {"S1": 35, "S2": 30, "S3": 24},
    "A3": {"S1": 34, "S2": 20, "S3": 14}
}

# Затраты для каждой стратегии
costs = {"A1": 120000, "A2": 80000, "A3": 45000}

# Константа для сдвига (чтобы все значения стали положительными)
shift_constant = 120000

# Определяем стратегии и ситуации
strategies = ["A1", "A2", "A3"]
situations = ["S1", "S2", "S3"]

# Инициализируем матрицу игры
game_matrix = np.zeros((3, 3))

# Преобразование в матрицу игры
for i, strat in enumerate(strategies):
    for j, sit in enumerate(situations):
        # Количество продукции на одну линию
        quantity = intensity_matrix[strat][sit]
        # Общая выработка (10 линий)
        total_production = 10 * quantity
        # Выручка
        revenue = total_production * 4
        # Прибыль
        profit = revenue - costs[strat]
        # Скорректированная прибыль
        adjusted_profit = profit + shift_constant
        # Заполняем матрицу
        game_matrix[i, j] = adjusted_profit

print("Матрица игры:\n", game_matrix)

# Решение для игрока A (максимизация v, т.е. минимизация -v)
c_A = [0, 0, 0, -1]  # Коэффициенты для p1, p2, p3, v
A_ub_A = np.array([
    [-game_matrix[0, 0], -game_matrix[1, 0], -game_matrix[2, 0], 1],
    [-game_matrix[0, 1], -game_matrix[1, 1], -game_matrix[2, 1], 1],
    [-game_matrix[0, 2], -game_matrix[1, 2], -game_matrix[2, 2], 1]
])
b_ub_A = [0, 0, 0]
A_eq_A = [[1, 1, 1, 0]]
b_eq_A = [1]

result_A = linprog(c_A, A_ub=A_ub_A, b_ub=b_ub_A, A_eq=A_eq_A, b_eq=b_eq_A, method='highs')
p1, p2, p3, v = result_A.x if result_A.success else [0, 0, 0, 0]

# Решение для игрока B (минимизация w)
c_B = [0, 0, 0, 1]  # Коэффициенты для q1, q2, q3, w
A_ub_B = np.array([
    [game_matrix[0, 0], game_matrix[0, 1], game_matrix[0, 2], -1],
    [game_matrix[1, 0], game_matrix[1, 1], game_matrix[1, 2], -1],
    [game_matrix[2, 0], game_matrix[2, 1], game_matrix[2, 2], -1]
])
b_ub_B = [0, 0, 0]
A_eq_B = [[1, 1, 1, 0]]
b_eq_B = [1]

result_B = linprog(c_B, A_ub=A_ub_B, b_ub=b_ub_B, A_eq=A_eq_B, b_eq=b_eq_B, method='highs')
q1, q2, q3, w = result_B.x if result_B.success else [0, 0, 0, 0]

# Вывод результатов
print(f"Вероятности для игрока A: p1={p1:.4f}, p2={p2:.4f}, p3={p3:.4f}")
print(f"Вероятности для игрока B: q1={q1:.4f}, q2={q2:.4f}, q3={q3:.4f}")
print(f"Цена игры (сдвинутая): {v:.2f}")
print(f"Фактическая цена игры: {v - shift_constant:.2f}")