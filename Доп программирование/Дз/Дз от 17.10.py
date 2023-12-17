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

# Пример использования
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Отсортированный список:", arr)

arr = [12, 11, 13, 5, 6]
subsequence_insertion_sort(arr, 1, 3)
print("Часть списка после сортировки:", arr)

#Сортировка выбором