def movimentaCavalo(posicao, numMov):
    if numMov == 1:
        return posicao[0] + 1, posicao[1] + 2
    elif numMov == 2:
        return posicao[0] + 2, posicao[1] + 1
    elif numMov == 3:
        return posicao[0] + 2, posicao[1] - 1
    elif numMov == 4:
        return posicao[0] + 1, posicao[1] - 2
    elif numMov == 5:
        return posicao[0] - 1, posicao[1] - 2
    elif numMov == 6:
        return posicao[0] - 2, posicao[1] - 1
    elif numMov == 7:
        return posicao[0] - 2, posicao[1] + 1
    elif numMov == 8:
        return posicao[0] - 1, posicao[1] + 2


num_movimentos = 0
buracos = [(1, 3), (2, 3), (2, 5), (5, 4)]
posicaoCavalo = (4, 3)
x = 4
y = 3

N = int(input().strip())
Movimentos = [int(M) for M in input().split()]

for Movimento in Movimentos:
    if posicaoCavalo in buracos:
        break
    else:
        num_movimentos += 1
        if Movimento == 1:
            posicaoCavalo = movimentaCavalo(posicaoCavalo, 1)
        elif Movimento == 2:
            posicaoCavalo = movimentaCavalo(posicaoCavalo, 2)
        elif Movimento == 3:
            posicaoCavalo = movimentaCavalo(posicaoCavalo, 3)
        elif Movimento == 4:
            posicaoCavalo = movimentaCavalo(posicaoCavalo, 4)
        elif Movimento == 5:
            posicaoCavalo = movimentaCavalo(posicaoCavalo, 5)
        elif Movimento == 6:
            posicaoCavalo = movimentaCavalo(posicaoCavalo, 6)
        elif Movimento == 7:
            posicaoCavalo = movimentaCavalo(posicaoCavalo, 7)
        elif Movimento == 8:
            posicaoCavalo = movimentaCavalo(posicaoCavalo, 8)

print(num_movimentos)
