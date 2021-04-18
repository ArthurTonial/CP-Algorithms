t = int(input())
while t:

    temp = input().split()
    zeros = int(temp[0])
    uns = int(temp[1])

    palavra = [x for x in input()]

    for x in palavra:
        if x == '0':
            zeros -= 1
        elif x == '1':
            uns -= 1

    tam = len(palavra)

    for i in range(tam//2):
        if palavra[i] != '?' and palavra[-i-1] == '?':
            palavra[-i-1] = palavra[i]
            if palavra[i] == "0":
                zeros -= 1
            else:
                uns -= 1
        elif palavra[i] == '?' and palavra[-i-1] != '?':
            palavra[i] = palavra[-i-1]
            if palavra[i] == '0':
                zeros -= 1
            else:
                uns -= 1

    for i in range(tam//2+1):
        if i == tam - i - 1 and palavra[i] == '?':
            if zeros == 1:
                palavra[i] = '0'
                zeros = 0
            elif uns == 1:
                palavra[i] = '1'
                uns = 0
        elif palavra[i] == palavra[-i-1] == '?':
            if zeros >= 2:
                palavra[i] = '0'
                palavra[-i-1] = '0'
                zeros -= 2
            else:
                palavra[i] = '1'
                palavra[-i-1] = '1'
                uns -= 2

    if palavra == palavra[::-1] and zeros == uns == 0:
        print("".join(palavra))
    else:
        print(-1)

    t -= 1
