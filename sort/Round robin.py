n = 3
bt = [5, 3, 8]
tq = 2

rem = bt.copy()
wt = [0]*n
time = 0

while sum(rem) > 0:
    for i in range(n):
        if rem[i] > 0:
            if rem[i] > tq:
                time += tq
                rem[i] -= tq
            else:
                time += rem[i]
                wt[i] = time - bt[i]
                rem[i] = 0

tat = [bt[i] + wt[i] for i in range(n)]

print("Process BT WT TAT")
for i in range(n):
    print("P", i+1, bt[i], wt[i], tat[i])

print("Average WT =", sum(wt)/n)
print("Average TAT =", sum(tat)/n)
