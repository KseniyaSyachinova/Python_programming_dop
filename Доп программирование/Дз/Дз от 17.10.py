#Сортировка вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def subsequence_insertion_sort(arr, start, end):
    for i in range(start + 1, end + 1):
        key = arr[i]
        j = i - 1
        while j >= start and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Отсортированный список:", arr)

arr = [12, 11, 13, 5, 6]
subsequence_insertion_sort(arr, 1, 3)
print("Часть списка после сортировки:", arr)

#Сортировка выбором
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def subsequence_selection_sort(arr, start, end):
    for i in range(start, end):
        min_idx = i
        for j in range(i+1, end+1):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Отсортированный список:", arr)

arr = [64, 25, 12, 22, 11]
subsequence_selection_sort(arr, 1, 3)
print("Часть списка после сортировки:", arr)

#Сортировка пузырьком
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def subsequence_bubble_sort(arr, start, end):
    for i in range(start, end):
        for j in range(start, end-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Отсортированный список:", arr)

arr = [64, 34, 25, 12, 22, 11, 90]
subsequence_bubble_sort(arr, 2, 5)
print("Часть списка после сортировки:", arr)