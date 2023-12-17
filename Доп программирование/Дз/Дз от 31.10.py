# Сортировка слиянием (делим массив пополам, рекурсивно сортируем обе половины, а затем сливаем их в отсортированный массив)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Находим середину массива
        left_half = arr[:mid]  # Делим массив на две части
        right_half = arr[mid:]

        # Рекурсивно вызываем merge_sort для каждой половины
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Слияние отсортированных половин
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Добавляем оставшиеся элементы, если таковые имеются
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print(arr)  # Выведет [3, 9, 10, 27, 38, 43, 82]

# "Быстрая сортировка"
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # Выбираем первый элемент в качестве опорного
        less = [x for x in arr[1:] if x <= pivot]  # Элементы меньше опорного
        greater = [x for x in arr[1:] if x > pivot]  # Элементы больше опорного
        return quick_sort(less) + [pivot] + quick_sort(greater)

arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = quick_sort(arr)
print(sorted_arr)  # Выведет [3, 9, 10, 27, 38, 43, 82]

# Пирамидальная сортировка
def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    l = 2 * i + 1  # Левый потомок
    r = 2 * i + 2  # Правый потомок

    # Если левый потомок существует и больше корня
    if l < n and arr[l] > arr[largest]:
        largest = l

    # Если правый потомок существует и больше корня
    if r < n and arr[r] > arr[largest]:
        largest = r

    # Если наибольший элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем местами корень и наибольший элемент
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Строим max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлекаем элементы по одному
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Меняем местами корень (максимальный элемент) и последний элемент
        heapify(arr, i, 0)


arr = [38, 27, 43, 3, 9, 82, 10]
heap_sort(arr)
print(arr)  # Выведет [3, 9, 10, 27, 38, 43, 82]

#DFS (поиск в глубину)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)  # Можно выполнить нужные действия с вершиной здесь

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(graph, 'A')

#BFS (поиск в ширину)
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex)  # Можно выполнить нужные действия с вершиной здесь

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')

# Оценка сложности графоф
# 1) Сортировка слиянием (Сложность состовляет O(nlogn) - самый эффективный алгоритм)
# 2) "Быстрая сортировка" (Сложность O(nlogn))
# 3) Пирамидальная сортировка Сложность O(nlogn))
# 4) DFS (Сложность O(n+m)) n - количество вершин, m - количество рёбер)
# 5) BFS (Сложность O(n+m)) n - количество вершин, m - количество рёбер)
# В сравнении с алгоритмами прошлого дз: сортировка вставками, Сортировка выбором, сортировка пузырьком, эти алгоритмы имеет
# более простую сложноть, с чем и связано их эффективность и применимость)