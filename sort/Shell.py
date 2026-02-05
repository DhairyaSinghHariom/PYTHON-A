def shellsort(arr):
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

# User input
arr = list(map(int, input("Enter numbers separated by space: ").split()))

print("Before Sorting:", arr)
shellsort(arr)
print("After Sorting :", arr)
