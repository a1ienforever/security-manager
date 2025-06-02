import numpy as np
from scipy.optimize import linprog

# Решение ЛП-задачи для игрока A (максимизация выигрыша)
def solve_lp_player_a(matrix):
    m, n = matrix.shape
    A = -matrix.T           # Преобразуем под задачу минимизации
    b = -np.ones(n)
    c = np.ones(m)          # Минимизируем сумму вероятностей, потом инвертируем

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')

    # Цена игры — обратная к целевой функции (по преобразованию)
    value = 1 / res.fun
    strategy = res.x * value  # Масштабируем вероятности

    return strategy, value

# Решение ЛП-задачи для игрока B (аналогично, но для столбцов)
def solve_lp_player_b(matrix):
    m, n = matrix.shape
    A = -matrix
    b = -np.ones(m)
    c = np.ones(n)

    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')

    value = 1 / res.fun
    strategy = res.x * value

    return strategy, value
