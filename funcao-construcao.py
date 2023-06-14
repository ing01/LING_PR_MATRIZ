matriz = []
m = int(input('Digite o numero de linhas: '))
n = int(input('Digite o numero de colunas: '))

def ler_matriz(): 
  for i in range(m): 
    linha = []
    for j in range(n): 
      x = int(input('Digite o elemento %i | %i da matriz: '%(i,j)))
      linha.append(x)
    matriz.append(linha)
  for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(matriz[i][j],end='\t')
    print('')

def main():
  ler_matriz()

main()
