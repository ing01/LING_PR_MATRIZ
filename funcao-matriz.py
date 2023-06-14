# Algoritmo contendo uma função/método que leia uma matriz.

def matriz(colunas, linhas):
  lista = []
  linha = []
  for c1 in range(0, linhas):
    linha = []
    for c2 in range(0, colunas):
        n = int(input('Número L[{0}] C[{1}]: '.format(c1 + 1,c2 + 1)))
        linha.append(n)
    lista.append(linha)
  print(lista)
  return lista

def main():
  nl = int(input('Quantas linhas? '))
  nc = int(input('Quantas colunas? '))
  matriz(nl, nc)

main()
