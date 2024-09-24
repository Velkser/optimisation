def my_sum(list_of_numbers):
    # Объявление переменных
    cdef int total = 0
    cdef int num
    
    # Суммирование элементов списка
    for num in list_of_numbers:
        total += num
    
    return total
