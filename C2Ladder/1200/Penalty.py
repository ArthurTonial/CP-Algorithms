LEN_KICKS = 10

def solve(kicks):
    
    win_a = ''
    win_b = ''
    for i in range(LEN_KICKS):
        if i % 2 == 0 and kicks[i] == '?':
            win_a += '1'
            win_b += '0'
        elif i % 2 == 1 and kicks[i] == '?':
            win_a += '0'
            win_b += '1'
        else:
            win_a += kicks[i]
            win_b += kicks[i]

    goals_a = 0
    goals_b = 0
    k_a = 5
    k_b = 5
    for i in range(LEN_KICKS):
        if i % 2 == 0:
            k_a -= 1
            if win_a[i] == '1':
                goals_a += 1
            if win_b[i] == '1':
                goals_b -= 1

        elif i % 2 != 0:
            k_b -= 1
            if win_a[i] == '1':
                goals_a -= 1
            if win_b[i] == '1':
                goals_b += 1

        if goals_a > k_b:
            return i+1

        if goals_b > k_a:
            return i+1

    return 10


t = int(input())

for i in range(t):
    s = input()

    print(solve(s))
    