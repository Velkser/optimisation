from numba import vectorize, int64, float64
import numpy as np
from my_time import timer

@timer
@vectorize([float64(float64, float64)])
def add_vectorized(a, b):
    return a + b

@timer
def add_lists(list1, list2):
    result = []
    # Итерация по индексам элементов исходных списков
    for i in range(len(list1)):
        # Добавление суммы элементов с соответствующими индексами
        result.append(list1[i] + list2[i])
    return result


# Пример использования векторизованной функции add_vectorized
arr1 = np.zeros(10000000)
arr2 = np.ones(10000000)
# print("Результат векторизованной функции add_vectorized:", add_vectorized(arr1, arr2))
# print("Результат функции add_lists:", add_lists(arr1, arr2))
add_vectorized(arr1, arr2)
add_lists(arr1, arr2)

