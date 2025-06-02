import numpy as np

# Входные данные
R1 = np.array([
    [0, 0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1]
])

R2 = np.array([
    [0, 1, 1, 1, 1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 1],
    [0, 1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1]
])

# 1.1 Пересечение
intersection = np.logical_and(R1, R2).astype(int)
intersection_pairs = np.sum(intersection)

# 1.2 Объединение
union = np.logical_or(R1, R2).astype(int)
union_pairs = np.sum(union)

# 1.3 Обращения
R1_transpose = R1.T
R2_transpose = R2.T
R1_transpose_pairs = np.sum(R1_transpose)
R2_transpose_pairs = np.sum(R2_transpose)

# 1.4 Композиции
# Уязвимость - угроза - уязвимость
R1_comp = np.dot(R1, R1_transpose)
R2_comp = np.dot(R2, R2_transpose)
R1_comp_pairs = np.sum(R1_comp > 0)
R2_comp_pairs = np.sum(R2_comp > 0)

# Угроза - уязвимость - угроза
R1_comp_threat = np.dot(R1_transpose, R1)
R2_comp_threat = np.dot(R2_transpose, R2)
R1_comp_threat_pairs = np.sum(R1_comp_threat > 0)
R2_comp_threat_pairs = np.sum(R2_comp_threat > 0)

# 2.1 Дополнение для R1
complement_R1 = (1 - R1).astype(int)
complement_R1_pairs = np.sum(complement_R1)

# 2.2 Двойственное отношение
complement_R1_transpose = complement_R1.T
dual_R1_pairs = np.sum(complement_R1_transpose)

# Вывод результатов
print("1.1 Пересечение:")
print(intersection)
print(f"Количество пар: {intersection_pairs}")
print("\n1.2 Объединение:")
print(union)
print(f"Количество пар: {union_pairs}")
print("\n1.3 Обращение R1:")
print(R1_transpose)
print(f"Количество пар: {R1_transpose_pairs}")
print("\n1.3 Обращение R2:")
print(R2_transpose)
print(f"Количество пар: {R2_transpose_pairs}")
print("\n1.4 Композиция (Уязвимость - угроза - уязвимость) R1:")
print(R1_comp)
print(f"Количество пар: {R1_comp_pairs}")
print("\n1.4 Композиция (Уязвимость - угроза - уязвимость) R2:")
print(R2_comp)
print(f"Количество пар: {R2_comp_pairs}")
print("\n1.4 Композиция (Угроза - уязвимость - угроза) R1:")
print(R1_comp_threat)
print(f"Количество пар: {R1_comp_threat_pairs}")
print("\n1.4 Композиция (Угроза - уязвимость - угроза) R2:")
print(R2_comp_threat)
print(f"Количество пар: {R2_comp_threat_pairs}")
print("\n2.1 Дополнение R1:")
print(complement_R1)
print(f"Количество пар: {complement_R1_pairs}")
print("\n2.2 Двойственное отношение R1:")
print(complement_R1_transpose)
print(f"Количество пар: {dual_R1_pairs}")