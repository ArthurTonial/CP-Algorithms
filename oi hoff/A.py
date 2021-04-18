t = int(input())

j = 1
while j <= t:

    n = int(input())

    lst = input().split(" ")

    ans = 0

    for i in range(len(lst)-1):
        if lst[i] != lst[i+1]:
            if i > 0:
                if lst[i] != lst[i-1]:
                    ans = i
                    break
                else:
                    ans = i + 1
                    break
            else:
                if lst[i+1] != lst[i+2]:
                    ans = i + 1
                    break
                else:
                    ans = i
                    break
    print(ans+1)
    j += 1
