# https://codeforces.com/problemset/problem/1472/D

# def solve(n, arr):
#     alice, bob = 0, 0

#     even_arr = [even for even in arr if even % 2 == 0]
#     odd_arr = [odd for odd in arr if odd % 2 != 0]

#     even_arr.sort(reverse=True)
#     e = 0
#     odd_arr.sort(reverse=True)
#     o = 0

#     turn = True
#     while e < len(even_arr) or o < len(odd_arr):

#         if turn:
#             if o == len(odd_arr):
#                 alice += even_arr[e]
#                 e += 1
#             elif e == len(even_arr):
#                 o += 1
#             elif even_arr[e] > odd_arr[o]:
#                 alice += even_arr[e]
#                 e += 1
#             else:
#                 o += 1
#         else:
#             if o == len(odd_arr):
#                 e += 1
#             elif e == len(even_arr):
#                 bob += odd_arr[o]
#                 o += 1
#             elif odd_arr[o] > even_arr[e]:
#                 bob += odd_arr[o]
#                 o += 1
#             else:
#                 e += 1
#         turn = not turn

#     if alice > bob:
#         return "Alice"
#     elif bob > alice:
#         return "Bob"
#     else:
#         return "Tie"

def solve(n, arr):
    arr = sorted(arr, reverse=True)

    ans = 0
    for i in range(n):
        if i % 2 == 0:
            if arr[i] % 2 == 0:
                ans += arr[i]
        else:
            if arr[i] % 2 != 0:
                ans -= arr[i]
    
    if ans == 0:
        return 'Tie'
    elif ans > 0:
        return 'Alice'
    else:
        return 'Bob'


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    print(solve(n, a))