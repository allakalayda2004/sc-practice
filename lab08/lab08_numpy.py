import numpy as np

# --- Задание 1 ---
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("Задание 1:")
print(f"hours: {hours}, shape: {hours.shape}, ndim: {hours.ndim}, size: {hours.size}, dtype: {hours.dtype}")

# --- Задание 2 ---
print("\nЗадание 2:")
print(f"Третий элемент: {hours[2]}")
print(f"Последний элемент: {hours[-1]}")
print(f"Элементы с 2 по 5: {hours[2:6]}")
print(f"Каждый второй: {hours[::2]}")
print(f"В обратном порядке: {hours[::-1]}")

# --- Задание 3 ---
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18]
])

print("\nЗадание 3:")
print(f"Форма: {temperatures.shape}, число измерений: {temperatures.ndim}, число элементов: {temperatures.size}")
print(f"Элемент (2, 3): {temperatures[1, 2]}")
print(f"Первая строка: {temperatures[0]}")
print(f"Последний столбец: {temperatures[:, -1]}")
print(f"Первые две строки без первого столбца: {temperatures[:2, 1:]}")
central = temperatures[:2, 1:3]
print(f"Центральный фрагмент: {central}")

# --- Задание 4 ---
matrix = np.arange(1, 26).reshape(5, 5)
print("\nЗадание 4:")
fragments = {
    "Первые три строки": matrix[:3, :],
    "Последние две строки": matrix[3:, :],
    "Первые два столбца": matrix[:, :2],
    "Строки 1-3, столбцы 2-4": matrix[1:4, 2:5],
    "Угловой блок 2x2": matrix[3:, 3:]
}
for name, frag in fragments.items():
    print(f"{name} (shape {frag.shape}):\n{frag}")

# --- Задание 5 ---
print("\nЗадание 5:")
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[1::2] = -1
print(f"changed_hours: {changed_hours}")
print(f"hours (исходный): {hours}")
# Комментарий: .copy() нужен, чтобы создать независимую копию массива в памяти,
# иначе изменение changed_hours приведет к изменению исходного массива hours.

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 188
print(f"changed_matrix:\n{changed_matrix}")

# --- Задание 6 ---
print("\nЗадание 6:")
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T
print(f"table:\n{table}\ntransposed:\n{transposed}")
# Комментарий: reshape(3, 4) работает, так как 3*4 = 12 элементов.
# reshape(5, 3) вызовет ошибку, так как 5*3 = 15, что не равно размеру массива (12).
