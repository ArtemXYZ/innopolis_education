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



# ============================= 3
# def fibonacci_search(arr, x):
#     n = len(arr)
#
#     # Первые числа Фибоначчи
#     fibM2 = 0  # (m-2)'th Fibonacci number
#     fibM1 = 1  # (m-1)'th Fibonacci number
#     fibM = fibM2 + fibM1  # m'th Fibonacci number
#
#     # fibM будет наименьшим числом Фибоначчи, больше или равным n
#     while fibM < n:
#         fibM2 = fibM1
#         fibM1 = fibM
#         fibM = fibM2 + fibM1
#
#     # Начальное смещение
#     offset = -1
#
#     while fibM > 1:
#         # Проверка безопасного индекса
#         i = min(offset + fibM2, n - 1)
#
#         # Если x больше, сдвигаем 3 числа Фибоначчи вниз
#         if arr[i] < x:
#             fibM = fibM1
#             fibM1 = fibM2
#             fibM2 = fibM - fibM1
#             offset = i
#
#         # Если x меньше, сдвигаем 2 числа Фибоначчи вниз
#         elif arr[i] > x:
#             fibM = fibM2
#             fibM1 = fibM1 - fibM2
#             fibM2 = fibM - fibM1
#
#         # Элемент найден
#         else:
#             return i
#
#     # Проверка последнего элемента
#     if fibM1 and arr[offset + 1] == x:
#         return offset + 1
#
#     # Элемент не найден
#     return -1
#
#
# # Пример использования
# arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
# x = 85
# print(f"Элемент найден на позиции: {fibonacci_search(arr, x)}")

# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.table = [[] for _ in range(size)]
#
#     def hash_function(self, key):
#         return hash(key) % self.size
#
#     def insert(self, key, value):
#         index = self.hash_function(key)
#         for kvp in self.table[index]:
#             if kvp[0] == key:
#                 kvp[1] = value
#                 return
#         self.table[index].append([key, value])
#
#     def search(self, key):
#         index = self.hash_function(key)
#         for kvp in self.table[index]:
#             if kvp[0] == key:
#                 return kvp[1]
#         return None
#
#     def delete(self, key):
#         index = self.hash_function(key)
#         for i, kvp in enumerate(self.table[index]):
#             if kvp[0] == key:
#                 del self.table[index][i]
#                 return
#
#
# # Пример использования
# hash_table = HashTable(10)
# hash_table.insert("apple", 1)
# hash_table.insert("banana", 2)
# hash_table.insert("orange", 3)
#
# print(f"Поиск 'apple': {hash_table.search('apple')}")
# print(f"Поиск 'banana': {hash_table.search('banana')}")
# print(f"Поиск 'grape': {hash_table.search('grape')}")
#
# hash_table.delete("banana")
# print(f"Поиск 'banana' после удаления: {hash_table.search('banana')}")

# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key

# def preorder_traversal(root):
#     if root:
#         print(root.val, end=" ")
#         preorder_traversal(root.left)
#         preorder_traversal(root.right)

# def inorder_traversal(root):
#     if root:
#         inorder_traversal(root.left)
#         print(root.val, end=" ")
#         inorder_traversal(root.right)

# def postorder_traversal(root):
#     if root:
#         postorder_traversal(root.left)
#         postorder_traversal(root.right)
#         print(root.val, end=" ")

#
# # Пример
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
#
# print("Префиксный обход:")
# preorder_traversal(root)

# print("\nИнфиксный обход:")
# inorder_traversal(root)

# print("\nПостфиксный обход:")
# postorder_traversal(root)

# class BST:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key
#
# def bst_insert(root, key):
#     if root is None:
#         return BST(key)
#
#     if key < root.val:
#         root.left = bst_insert(root.left, key)
#     else:
#         root.right = bst_insert(root.right, key)
#
#     return root
#
# def bst_search(root, key):
#     if root is None or root.val == key:
#         return root
#
#     if key < root.val:
#         return bst_search(root.left, key)
#
#     return bst_search(root.right, key)
#
# # Пример
# root = BST(50)
# bst_insert(root, 30)
# bst_insert(root, 20)
# bst_insert(root, 40)
# bst_insert(root, 70)
# bst_insert(root, 60)
# bst_insert(root, 80)
#
# key = 40
# result = bst_search(root, key)
# if result:
#     print(f"\nKey {key} found in BST")
# else:
#     print(f"\nKey {key} not found in BST")


# def naive_search(text, pattern):
#     n = len(text)
#     m = len(pattern)
#
#     for i in range(n - m + 1):
#         j = 0
#         while j < m and text[i + j] == pattern[j]:
#             j += 1
#         if j == m:
#             print(f"Pattern found at index {i}")
#
# # Пример использования
# text = "ABABDABACDABABCABAB"
# pattern = "ABABCABAB"
# naive_search(text, pattern)


# def kmp_search(text, pattern):
#     def compute_lps(pattern):
#         lps = [0] * len(pattern)
#         length = 0
#         i = 1
#         while i < len(pattern):
#             if pattern[i] == pattern[length]:
#                 length += 1
#                 lps[i] = length
#                 i += 1
#             else:
#                 if length != 0:
#                     length = lps[length - 1]
#                 else:
#                     lps[i] = 0
#                     i += 1
#         return lps
#
#     n = len(text)
#     m = len(pattern)
#     lps = compute_lps(pattern)
#
#     i = 0  # index for text
#     j = 0  # index for pattern
#     while i < n:
#         if pattern[j] == text[i]:
#             i += 1
#             j += 1
#
#         if j == m:
#             print(f"Pattern found at index {i - j}")
#             j = lps[j - 1]
#         elif i < n and pattern[j] != text[i]:
#             if j != 0:
#                 j = lps[j - 1]
#             else:
#                 i += 1
#
# # Пример использования
# text = "ABABDABACDABABCABAB"
# pattern = "ABABCABAB"
# kmp_search(text, pattern)