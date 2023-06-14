# Função que recebe uma matriz e returne True se a matriz for simetrica, em caso contrario retorna False. Uma matriz é considerada simétrica quando a 
# quantidade de linhas é igual a da coluna.

def matriz():
  linha = []
  lista = []
  nl = int(input('Quantas linhas? '))
  nc = int(input('Quantas colunas? '))
  for c1 in range(0, nl):
    linha = []
    for c2 in range(0, nc):
        n = int(input('Número L[{0}] C[{1}]: '.format(c1 + 1,c2 + 1)))
        linha.append(n)
    lista.append(linha)
  print(lista)
  if nl == nc:
    return True
  else:
    return False

def main():
  m = matriz()
  print(m)

main()
