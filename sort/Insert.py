# Insertion sort
def insertion(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Example

arr = [8, 3, 5, 2]

for i in range(1, len(arr)):
    key = arr[i]      # element to insert
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]   # shift right
        j -= 1

    arr[j + 1] = key          # insert element

print(arr)




# Bubble Sort 
"""Compare first two numbers

Swap if the first is bigger

Move to the next pair

Repeat until the list is sorted
"""


arr = [5, 3, 8, 4, 2]
n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted list:", arr)


# Seletion Sort

arr = [5, 3, 8, 4, 2]
n = len(arr)

for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted list:", arr)



