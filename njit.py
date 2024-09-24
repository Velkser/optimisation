from my_time import timer
from numba import njit


# Декоратор @njit применяется к функции для ее компиляции с использованием Numba без Python-режима
@timer
@njit
def add_with_njit(a, b):
    result = 0
    for _ in range(100000000):  # Вложенный цикл для создания нагрузки
        result += a + b
    return result

# Обычная функция без декоратора
@timer
def add_without_njit(a, b):
    result = 0
    for _ in range(100000000):  # Вложенный цикл для создания нагрузки
        result += a + b
    return result


res1 = add_with_njit(1,2)
res2 = add_without_njit(1,2)