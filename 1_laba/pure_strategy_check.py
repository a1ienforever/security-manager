def check_pure_strategy_equilibrium(matrix):
    # Минимумы по строкам — гарантированный минимум для игрока A
    row_mins = matrix.min(axis=1)
    # Максимумы по столбцам — наихудший случай для B (макс. потери A)
    col_maxs = matrix.max(axis=0)

    lower_value = row_mins.max()  # Нижняя цена игры (максимум из минимумов строк)
    upper_value = col_maxs.min()  # Верхняя цена игры (минимум из максимумов столбцов)

    has_saddle_point = lower_value == upper_value  # Седловая точка существует, если цены равны

    return {
        "row_mins": row_mins,
        "col_maxs": col_maxs,
        "lower_value": lower_value,
        "upper_value": upper_value,
        "has_saddle_point": has_saddle_point
    }
