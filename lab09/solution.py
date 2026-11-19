import numpy as np

def make_hours():
    # Возвращает вектор [0, 3, 6, 9, 12, 15, 18, 21]
    return np.arange(0, 22, 3).tolist()

def vector_report(values):
    arr = np.asarray(values)
    return {
        "third": float(arr[2]),
        "last": float(arr[-1]),
        "middle": arr[2:6].tolist(),
        "every_second": arr[::2].tolist(),
        "reversed": arr[::-1].tolist()
    }

def change_vector(values):
    arr = np.array(values).copy()
    # Заменяем элементы с индексами 2, 3, 4 на 99
    arr[2:5] = 99
    # Заменяем каждый второй элемент на -1
    arr[::2] = -1
    return arr.tolist()

def cap_above(values, limit):
    arr = np.array(values).copy()
    # Используем маску для замены значений > limit на limit
    arr[arr > limit] = limit
    return arr.tolist()

def celsius_to_fahrenheit(values):
    arr = np.asarray(values)
    # Перевод по формуле без циклов
    fahrenheit = arr * 9 / 5 + 32
    return fahrenheit.tolist()
