t = int(input())

while t:
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()

    b1, b2 = a[-1], a[-2]

    somatorio = sum(a)

    if somatorio - b1 == 2 * b2:
        a = [str(x) for x in a[:n]]
        print(" ".join(a))
    else:
        for i in range(n+1):
            if somatorio - a[i] == 2 * b1:
                b = a[:i] + a[i+1:n+1]
                b = [str(x) for x in b[:n]]
                print(" ".join(b))
                break
        else:
            print("-1")

    t -= 1
