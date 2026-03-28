def bankers_algorithm():
    n = 5  # number of processes
    m = 3  # number of resources

    allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    max_need = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]

    available = [3, 3, 2]

    # Calculate Need matrix
    need = [[max_need[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]

    finish = [False] * n
    safe_sequence = []
    work = available.copy()

    while len(safe_sequence) < n:
        found = False

        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):
                    
                    # Allocate resources
                    for j in range(m):
                        work[j] += allocation[i][j]

                    safe_sequence.append(i)
                    finish[i] = True
                    found = True

        if not found:
            print("System is NOT in safe state")
            return

    print("System is in SAFE state")
    print("Safe sequence:", ["P" + str(i) for i in safe_sequence])


# Run the algorithm
bankers_algorithm()