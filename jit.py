from numba import jit
from my_time import timer

# Функция с декоратором @jit
@timer
@jit
def add_with_jit(a: int, b: int):
    result = 0
    for _ in range(100000000):  # Вложенный цикл для создания нагрузки
        result += a + b
    return result

# Обычная функция без декоратора
@timer
def add_without_jit(a, b):
    result = 0
    for _ in range(100000000):  # Вложенный цикл для создания нагрузки
        result += a + b
    return result

res1 = add_with_jit(1,2)
res2 = add_without_jit(1,2)