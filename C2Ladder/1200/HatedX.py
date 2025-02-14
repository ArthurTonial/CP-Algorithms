# https://codeforces.com/problemset/problem/1364/A

def solve(hated_n, arr, size):
    acc = sum(arr)

    if acc % hated_n != 0:
        return size

    l = 0
    suffix = acc
    while suffix % hated_n == 0 and l < size:
        suffix -= arr[l]
        l += 1

    r = size - 1
    prefix = acc
    while prefix % hated_n == 0 and r > -1:
        prefix -= arr[r]
        r -= 1

    if r == -1 and l == size:
        return -1
    return max(size - l, size - (size - r) + 1)
    

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(x, a, n))