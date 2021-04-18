import math

for t in range(int(input())):

    n, c = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    b.append(0)

    days = 10**10
    dol = 0
    k = 0
    for i in range(n):
        if dol >= c:
            days = min(days, k)
        else:
            days = min(days, k + int(math.ceil((c-dol)/a[i])))

        if dol >= b[i]:
            dol -= b[i]
            k += 1
        else:
            k += 1 + int(math.ceil((b[i]-dol)/a[i]))
            dol = int(math.ceil((b[i]-dol)/a[i])) * a[i] - (b[i] - dol)

    print(days)
