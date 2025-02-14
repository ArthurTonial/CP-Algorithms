# https://codeforces.com/problemset/problem/1272/B

def solve(instructions):
    l, r, u, d = 0, 0, 0, 0
    for i in instructions:
        if i == 'L':
            l += 1
        elif i == 'R':
            r += 1
        elif i == 'U':
            u += 1
        else:
            d += 1

    l = r = min(l, r)
    u = d = min(u, d)

    if l == 0 and u > 1:
        print(2)
        print('UD')
        return
    
    if u == 0 and l > 1:
        print(2)
        print('LR')
        return
    
    print(l+r+u+d)
    print('L' * l + 'U' * u + 'R' * r + 'D' * d)   


q = int(input())

for _ in range(q):
    s = input()
    solve(s)

