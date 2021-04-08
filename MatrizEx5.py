##Crie uma função que a partir de uma matriz 4x4 mostre a soma dos elementos da diagonal principal . Mostre também a soma dos elementos que estão acima da diagonal principal. 
##Diagonal principal é identificada pelos elementos que estão no mesmo índice de linha e coluna, exemplo, [1,1], [2,2], etc.

matriz=[]

def ma():
  for i in range(4):
    linha=[]
    for j in range(4):
      x = int(input('digite um valor para %i | %i: '%(i,j)))
      linha.append(x)
    matriz.append(linha)
  for i in range(4):
    for j in range(4):
      print(matriz[i][j], end='\t')
    print(' ')
  soma = 0
  for j in range(0,4):
    soma += matriz[0][j]
  print('a soma a cima é: ',soma)
  cont = 0
  for i in range(4):
    for j in range(4):
      if matriz[i] == matriz[j]:
        cont+= matriz[i][j]
  print('a soma da diagonal perfeit é: ',cont)

def main():
  ma()

main()
