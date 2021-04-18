for t in range(int(input())):

    n, l, r, s = map(int, input().split())

    tam = r-l+1

    if s < tam*(tam+1)/2 or s > (n-tam)*tam + tam*(tam+1)/2:
        print('-1')
    else:
        rl_list = [x for x in range(1, tam+1)]
        soma = sum(rl_list)
        aux = n
        for i in range(tam-1, -1, -1):
            while rl_list[i] < aux and soma != s:
                rl_list[i] += 1
                soma += 1
            aux -= 1
            if soma == s:
                break

        aux = 1
        for i in range(l - 1):
            while aux in rl_list:
                aux += 1
            rl_list.insert(i, aux)
        for i in range(r, n):
            while aux in rl_list:
                aux += 1
            rl_list.append(aux)
        rl_list = map(str, rl_list)
        print(" ".join(rl_list))
