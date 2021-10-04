N = int(input())
while N < 3 or N > 10000:
     N = int(input())
Fita = input().split()

#verificando se há pelo menos um "0" na Fita
encontrou = 0
while encontrou == 0:
     for elem in Fita:
          if int(elem) == 0:
               encontrou = 1
               break
     if encontrou == 0:
          Fita = input().split()

#Varrendo os elementos
i = 0
for i in range(N):
     if int(Fita[i]) == -1:
          #Distancia de Fita[i] até o próximo 0
          Dd = 0
          #indice da direita
          indiceD = i
          #percorrer a Fita de "i" até o final dela
          for indiceD in range(i, N):
               if int(Fita[indiceD]) == 0:
                    Dd = indiceD - i
                    break
               
          #Distancia de Fita[i] até o 0 anterior
          De = 0
          #indice da esquerda
          indiceE = i
          #percorrer a Fita a partir de "i" até seu início
          for indiceE in range(i, -1, -1):
               if int(Fita[indiceE]) == 0:
                    De = i - indiceE
                    break

          #Definindo a menor distãncia
          if Dd != 0 and De !=0:
               if Dd < De:
                    Fita[i] = Dd
               else:
                    Fita[i] = De
          elif Dd != 0 and De == 0:
               Fita[i] = Dd
          elif De != 0 and Dd == 0:
               Fita[i] = De
#Printando a Fita colorida sequencialmente
for elem in Fita:
     print(f'{elem}', end=" ") 
