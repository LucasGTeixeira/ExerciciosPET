def quadrado_magico():
        matriz = []
        N = int(input())
        i = 0
        while N < 2 or N > 10:
                N = int(input())  
        for i in range(N):
                input_linha = str(input()).split()
                matriz.append(input_linha)
                        
        #soma das linhas
        Somas_Linhas = []
        i = 0
        for linha in matriz:
                soma = 0
                for i in range(N):
                        soma += int(linha[i])
                Somas_Linhas.append(soma)
        #conferindo se a soma das linhas é a mesma
        for i in range(N-1):
                if (Somas_Linhas[i] != Somas_Linhas[i+1]):
                        return -1

        #soma das colunas
        Somas_Colunas = []
        j = 0
        for i in range(N):
                soma = 0
                for j in range(N):
                        soma += int(matriz[j][i])
                Somas_Colunas.append(soma)
        #conferindo se a soma das colunas é a mesma
        for i in range(N-1):
                if (Somas_Colunas[i] != Somas_Colunas[i+1]):
                        return -2

        #soma diagonais
        soma_diagonal1 = 0
        soma_diagonal2 = 0
        cont = 0
        for i in range(N):
                soma_diagonal1 += int(matriz[i][0+cont])
                soma_diagonal2 += int(matriz[i][(N-1)-cont])
                cont += 1
        #conferindo se a soma das diagonais é a mesma
        if (soma_diagonal1 != soma_diagonal2):
                return -3
     
        #comparando somas
        if (soma_diagonal1 == Somas_Colunas[0] and Somas_Colunas[0] == Somas_Linhas[0]):
                return Somas_Linhas[0]

print(quadrado_magico())
     

