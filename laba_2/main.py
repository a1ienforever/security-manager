from game_matrix import game_matrix
from pure_strategy_check import check_pure_strategy_equilibrium
from solve_lp import solve_lp_player_a, solve_lp_player_b
import numpy as np

def main():
    print("Исходная матрица игры:\n", game_matrix)

    # Шаг 1: Проверка на равновесие в чистых стратегиях
    result = check_pure_strategy_equilibrium(game_matrix)
    print("\nПроверка равновесия в чистых стратегиях:")
    print("Минимумы по строкам (для A):", result["row_mins"])
    print("Максимумы по столбцам (для B):", result["col_maxs"])
    print("Нижняя цена игры:", result["lower_value"])
    print("Верхняя цена игры:", result["upper_value"])

    if result["has_saddle_point"]:
        print("Седловая точка существует — игра решается в чистых стратегиях.")
    else:
        print("Седловой точки нет — решаем через линейное программирование.")

        # Шаг 2: ЛП для игрока A
        print("\nРешение ЛП-задачи для игрока A:")
        strategy_a, value_a = solve_lp_player_a(game_matrix)
        print("Смешанная стратегия A (вероятности):", np.round(strategy_a, 4))
        print("Цена игры (выигрыш для A):", round(value_a, 4))

        # Шаг 3: ЛП для игрока B
        print("\n Решение ЛП-задачи для игрока B:")
        strategy_b, value_b = solve_lp_player_b(game_matrix)
        print("Смешанная стратегия B (вероятности):", np.round(strategy_b, 4))
        print("Цена игры (проигрыш для B):", round(value_b, 4))

if __name__ == "__main__":
    main()
