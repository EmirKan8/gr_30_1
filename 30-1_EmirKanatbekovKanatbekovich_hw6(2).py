def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(element, arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1

    return -1


unsorted_list = [5, 2, 9, 1, 7]
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)

element_to_find = 9
index = binary_search(element_to_find, sorted_list)
if index != -1:
    print(f"Элемент {element_to_find} найден по индексу {index}.")
else:
    print(f"Элемент {element_to_find} не найден.")