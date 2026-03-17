n = int(input("Enter number of processes: "))

bt = []
for i in range(n):
    bt.append(int(input(f"Burst Time of P{i+1}: ")))

wt = [0]*n
tat = [0]*n

for i in range(1, n):
    wt[i] = wt[i-1] + bt[i-1]

for i in range(n):
    tat[i] = wt[i] + bt[i]

print("\nP\tBT\tWT\tTAT")
for i in range(n):
    print(f"P{i+1}\t{bt[i]}\t{wt[i]}\t{tat[i]}")

print("\nAverage WT =", sum(wt)/n)
print("Average TAT =", sum(tat)/n)
