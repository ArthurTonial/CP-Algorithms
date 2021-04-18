t = int(input())

i = 1
while i <= t:

    lst = []
    n = int(input())
    for j in range(n):
        lst2 = [x for x in input()]
        lst.append(lst2)

    n = len(lst)

    x1 = -1
    y1 = -1
    x2 = -1
    y2 = -1
    for y in range(n):
        for x in range(n):
            if lst[x][y] == '*':
                if x1 == -1:
                    x1 = x
                    y1 = y
                else:
                    x2 = x
                    y2 = y

    if x1 == x2:
        if x1 + 1 == n:
            lst[x1 - 1][y1] = '*'
            lst[x2 - 1][y2] = '*'
        else:
            lst[x1 + 1][y1] = '*'
            lst[x2 + 1][y2] = '*'

    elif y1 == y2:
        if y1 + 1 == n:
            lst[x1][y1 - 1] = '*'
            lst[x2][y1 - 1] = '*'
        else:
            lst[x1][y1 + 1] = '*'
            lst[x2][y1 + 1] = '*'

    else:
        lst[x1][y2] = '*'
        lst[x2][y1] = '*'

    for y, linha in enumerate(lst):
        for x in linha:
            print(x, end='')
        if not (i == t and y == n-1):
            print()
    i += 1
