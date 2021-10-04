def pulo_do_gato():
     C = int(input())
     while C < 1 and C > 10000:
          C = int(input())
     Lajotas = str(input()).split()
     while Lajotas[0] == '0' or Lajotas[len(Lajotas)-1] == '0':
          Lajotas = input().split()    
   
     i = 0
     cont = 0
     while i < C-2:
          if Lajotas[i] == '1' and Lajotas[i+2] == '1':
               cont += 1
               i += 2
          elif Lajotas[i] == '1' and Lajotas[i+1] == '1' and Lajotas[i+2] == '0':
               cont += 1
               i += 1
          elif Lajotas[i] == '1' and Lajotas[i+1] == '0' and Lajotas[i+2] == '0':
               return -1
     if i == C-2:
          cont += 1
     return cont

print(pulo_do_gato())
     
