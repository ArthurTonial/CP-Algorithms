# https://codeforces.com/problemset/problem/1537/C

def solve(heights):
    heights = sorted(heights)

    if len(heights) == 2:
        print(f'{heights[0]} {heights[1]}')
        return

    first = 0
    last = 1
    for i in range(2, len(heights)):
        if abs(heights[i] - heights[i-1]) < abs(heights[last] - heights[first]):
            first = i-1
            last = i
    ans = heights[last:] + heights[:first+1]  

    for a in ans:
        print(a, end=' ')
    print()


t = int(input())

for _ in range(t):
    n = int(input())
    h = [int(x) for x in input().split()]
    solve(h)
 