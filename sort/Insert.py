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
