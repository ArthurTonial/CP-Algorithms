# https://codeforces.com/problemset/problem/1520/D

def solve(arr):
    dict_diffs = {}
    
    for i in range(len(arr)):
        dict_diffs[arr[i] - i] = dict_diffs.get(arr[i] - i, 0) + 1

    ans = 0
    for k, v in dict_diffs.items():
        ans += v * (v-1) / 2
    print(int(ans))


t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    solve(a)
