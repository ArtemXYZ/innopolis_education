# # import matplotlib.pyplot as plt
# import numpy as np
# import time
# import sys
# Устанавливаем максимальное количество цифр для строкового представления целого числа
# sys.set_int_max_str_digits(10000)


#
# # ====
# import time
#
# import matplotlib.pyplot as plt
# import sys
# import numpy as np
#
# # Устанавливаем максимальное количество цифр для строкового представления целого числа
# sys.set_int_max_str_digits(10000)
#
#
#
# def binary_search(arr, x):
#     left, right = 0, len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         # Проверка среднего элемента
#         if arr[mid] == x:
#             return mid
#
#         # Если x больше, игнорируем левую половину
#         elif arr[mid] < x:
#             left = mid + 1
#         # Если x меньше, игнорируем правую половину
#         else:
#             right = mid - 1
#
#     # Элемент не найден
#     return -1
#
#
#
# def karatsuba(x, y):
#     # Базовый случай для рекурсии
#     if x < 10 or y < 10:
#         return x * y
#
#     # Определяем наибольшее количество цифр
#     n = max(len(str(x)), len(str(y)))
#     half_n = n // 2
#
#     # Делим x и y на части
#     high1, low1 = divmod(x, 10 ** half_n)
#     high2, low2 = divmod(y, 10 ** half_n)
#
#     # Рекурсивные вызовы для частей чисел
#     z0 = karatsuba(low1, low2)
#     z1 = karatsuba((low1 + high1), (low2 + high2))
#     z2 = karatsuba(high1, high2)
#
#     # Комбинируем результаты
#     return (z2 * 10 ** (2 * half_n)) + ((z1 - z2 - z0) * 10 ** half_n) + z0
#
#
# # Функция для замера времени выполнения
# def measure_time(func, *args):
#     start_time = time.time()
#     result = func(*args)
#     end_time = time.time()
#     return end_time - start_time, result
#
#
# # Размеры чисел для тестирования
# sizes = [10, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
#
# # Списки для хранения времени выполнения
# karatsuba_times = []
#
# # Тестирование алгоритмов на различных размерах чисел
# for size in sizes:
#     x = int('9' * size)
#     y = int('8' * size)
#
#     time_karatsuba, result_karatsuba = measure_time(karatsuba, x, y)
#
#     karatsuba_times.append(time_karatsuba)
#
# # Построение графиков
# plt.figure(figsize=(10, 6))
# plt.plot(sizes, karatsuba_times, label='Алгоритм Карацупы', marker='o')
# plt.xlabel('Количество чисел')
# plt.ylabel('Время (секунды)')
# plt.title('Временная сложность умножения Карацубы')
# plt.legend()
# plt.grid(True)
# plt.yscale('log')
# plt.show()
#
#
#
# # Размер массива
# n = np.arange(1, 10001)  # от 1 до 10000
#
# # Временные затраты для линейного поиска
# linear_time = n
#
# # Временные затраты для бинарного поиска
# binary_time = np.log2(n)
#
# # Создание графика
# plt.figure(figsize=(10, 6))
# plt.plot(n, linear_time, label='Линейный поиск (O(n))', color='blue')
# plt.plot(n, binary_time, label='Бинарный поиск (O(log n))', color='red')
# plt.ylim(0, max(linear_time))  # Ограничиваем ось y для лучшего отображения
# plt.xlabel('Размер массива (n)')
# plt.ylabel('Время выполнения')
# plt.title('Сравнение времени выполнения линейного и бинарного поиска')
# plt.legend()
# plt.grid(True)
# plt.show()
#
#
# def binary_search(arr, x):
#     left, right = 0, len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         # Проверка среднего элемента
#         if arr[mid] == x:
#             return mid
#         # Если x больше, игнорируем левую половину
#         elif arr[mid] < x:
#             left = mid + 1
#         # Если x меньше, игнорируем правую половину
#         else:
#             right = mid - 1
#
#     # Элемент не найден
#     return -1
#
#
# # Пример использования
# arr = [2, 3, 4, 10, 40]
# x = 10
#
# result = binary_search(arr, x)
# if result != -1:
#     print(f"Элемент найден на индексе {result}")
# else:
#     print("Элемент не найден в массиве")
#
# import timeit
# import matplotlib.pyplot as plt
# import numpy as np
#
#
# def binary_search(arr, x):
#     left, right = 0, len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return -1
#
#
# def measure_time(n, repetitions=100):
#     arr = list(range(n))  # Создаем отсортированный массив от 0 до n-1
#     x = n // 2  # Искомый элемент, который гарантированно находится в массиве
#
#     # Время выполнения в миллисекундах
#     stmt = lambda: [binary_search(arr, x) for _ in range(repetitions)]
#     setup = 'from __main__ import binary_search'
#     time_taken = timeit.timeit(stmt, setup, number=1)  # Выполняем все повторения за один вызов
#
#     # Возвращаем среднее время выполнения на одну операцию
#     return time_taken / repetitions
#
#
# # Создаем данные для графика
# sizes = np.arange(1000000, 10000001, 1000000)  # Размер массива от 1000000 до 10000000, с шагом 1000000
# times = []
#
# for size in sizes:
#     time_taken = measure_time(size)
#     times.append(time_taken)
#     print(f"Размер массива: {size}, Время выполнения: {time_taken:.6f} сек")
#
# # Вычисляем теоретическую оценку сложности
# theoretical_times = [np.log2(size) / 1000000 for size in sizes]  # Уменьшено для масштаба
#
# # Построение графика
# plt.figure(figsize=(12, 8))
# plt.plot(sizes, times, label='Фактическое время выполнения бинарного поиска', color='blue', linestyle='-', marker='o')
# plt.plot(sizes, theoretical_times, label='Теоретическая оценка сложности O(log n)', color='red', linestyle='--')
#
# plt.xlabel('Размер массива (n)')
# plt.ylabel('Время выполнения (сек)')
# plt.title('Оценка сложности бинарного поиска')
# plt.legend()
# plt.grid(True)
# plt.show()
#
#
# import timeit
# import matplotlib.pyplot as plt
# import numpy as np
#
#
# def linear_search(arr, x):
#     for index, value in enumerate(arr):
#         if value == x:
#             return index
#     return -1
#
# def binary_search(arr, x):
#     left, right = 0, len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return -1
# def measure_time_search(search_function, n, repetitions=100):
#     arr = list(range(n))  # Создаем отсортированный массив от 0 до n-1
#     x = n // 2  # Искомый элемент, который гарантированно находится в массиве
#
#     # Время выполнения в миллисекундах
#     stmt = lambda: [search_function(arr, x) for _ in range(repetitions)]
#     setup = f'from __main__ import {search_function.__name__}'
#     time_taken = timeit.timeit(stmt, setup, number=1)  # Выполняем все повторения за один вызов
#
#     # Возвращаем среднее время выполнения на одну операцию
#     return time_taken / repetitions
#
#
# Создаем данные для графика
# sizes = np.arange(10000, 100001, 10000)  # Размер массива от 1000000 до 10000000, с шагом 1000000
# binary_times = []
# linear_times = []
#
# for size in sizes:
#     # Измеряем время выполнения бинарного поиска
#     binary_time_taken = measure_time_search(binary_search, size)
#     binary_times.append(binary_time_taken)
#
#     # Измеряем время выполнения линейного поиска
#     linear_time_taken = measure_time_search(linear_search, size)
#     linear_times.append(linear_time_taken)
#
#     print(
#         f"Размер массива: {size}, Время бинарного поиска: {binary_time_taken:.6f} сек, Время линейного поиска: {linear_time_taken:.6f} сек")
#
# # Вычисляем теоретическую оценку сложности
# theoretical_binary_times = [np.log2(size) / 1000000 for size in sizes]  # Уменьшено для масштаба
# theoretical_linear_times = [size / 1000000 for size in sizes]  # Масштабируем для масштаба
#
# # Построение графика
# plt.figure(figsize=(14, 10))
# plt.plot(sizes, binary_times, label='Фактическое время бинарного поиска', color='blue', linestyle='-', marker='o')
# plt.plot(sizes, linear_times, label='Фактическое время линейного поиска', color='green', linestyle='-', marker='x')
# plt.plot(sizes, theoretical_binary_times, label='Теоретическая оценка бинарного поиска O(log n)', color='red',
#          linestyle='--')
# plt.plot(sizes, theoretical_linear_times, label='Теоретическая оценка линейного поиска O(n)', color='orange',
#          linestyle='--')
#
# plt.xlabel('Размер массива (n)')
# plt.ylabel('Время выполнения (сек)')
# plt.title('Сравнение времени выполнения бинарного и линейного поиска')
# plt.legend()
# plt.grid(True)
# plt.show()
# ================================
# # сортировка пузырьком
#
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr

#
# result = bubble_sort([5, 1, 4, 2, 8])
# print(result)
# # Исходный массив: [5, 1, 4, 2, 8]
# # Шаг 1: [1, 5, 4, 2, 8]
# # Шаг 2: [1, 4, 5, 2, 8]
# # Шаг 3: [1, 4, 2, 5, 8]
# # Шаг 4: [1, 2, 4, 5, 8]

# # сортировка вставками ***
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr
#
#
# result = insertion_sort([12, 11, 13, 5, 6])
# print(result)
# # Исходный массив: [12, 11, 13, 5, 6]
# # Шаг 1: [11, 12, 13, 5, 6]
# # Шаг 2: [11, 12, 13, 5, 6]
# # Шаг 3: [5, 11, 12, 13, 6]
# # Шаг 4: [5, 6, 11, 12, 13]
#
#
# # сортировка выбором
# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr
#
#
# result = selection_sort([29, 10, 14, 37, 13])
# print(result)
#
# # Исходный массив: [29, 10, 14, 37, 13]
# # Шаг 1: [10, 29, 14, 37, 13]
# # Шаг 2: [10, 13, 14, 37, 29]
# # Шаг 3: [10, 13, 14, 37, 29]
# # Шаг 4: [10, 13, 14, 29, 37]


# сортировка Шелла
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr


result = shell_sort([23, 12, 1, 8, 34, 54, 2, 3])
print(result)
# Исходный массив: [23, 12, 1, 8, 34, 54, 2, 3]
# Gap = 4: [8, 2, 1, 3, 23, 12, 34, 54]
# Gap = 2: [1, 2, 3, 8, 12, 23, 34, 54]
# Gap = 1: [1, 2, 3, 8, 12, 23, 34, 54]


import time
import random

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())
    return time.time() - start_time

# Создание случайного массива
arr = [random.randint(0, 10000) for _ in range(1000)]

# Сравнение алгоритмов
print(f"Пузырьковая сортировка: {measure_time(bubble_sort, arr)} секунд")
print(f"Сортировка вставками: {measure_time(insertion_sort, arr)} секунд")
print(f"Сортировка выбором: {measure_time(selection_sort, arr)} секунд")
print(f"Сортировка Шелла: {measure_time(shell_sort, arr)} секунд")