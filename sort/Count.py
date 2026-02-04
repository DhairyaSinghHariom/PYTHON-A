def counting_sort(arr):
    max_val = max(arr)

    # Create count array
    count = [0] * (max_val + 1)

    # Count each number
    for num in arr:
        count[num] += 1

    # Build sorted array
    a= []
    for i in range(len(count)):
        a.extend([i] * count[i])

    return a


# User input
arr = list(map(int, input("Enter numbers separated by space: ").split()))

result = counting_sort(arr)
print("Sorted Array:", result)
