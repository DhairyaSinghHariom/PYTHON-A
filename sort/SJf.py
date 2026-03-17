n = 3

bt = [5, 2, 8]

# sort burst time
bt.sort()

wt = [0] * n
tat = [0] * n

# Waiting Time
for i in range(1, n):
    wt[i] = wt[i-1] + bt[i-1]

# Turnaround Time
for i in range(n):
    tat[i] = wt[i] + bt[i]

print("Process  BT  WT  TAT")

for i in range(n):
    print("P", i+1, "   ", bt[i], "  ", wt[i], "  ", tat[i])

print("Average Waiting Time =", sum(wt)/n)
print("Average Turnaround Time =", sum(tat)/n)
