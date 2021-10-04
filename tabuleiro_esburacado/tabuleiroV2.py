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

N = int(input().strip())
Movimentos = [int(M) for M in input().split()]

for Movimento in Movimentos:
    if posicaoCavalo in buracos:
        break
    else:
        num_movimentos += 1
        posicaoCavalo = movimentaCavalo(posicaoCavalo, Movimento)

print(num_movimentos)
