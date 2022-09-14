matriz = []
soma = []
linhas = int (input("Digite o numero pedido de linhas da Matriz:"))
colunas = int (input("Digite o numero pedido de colunas da Matriz:"))

def contrutorMatriz (linhas, colunas, matriz):
    for i in range(1, linhas+1):
        naLinha = []
        for j in range (1, colunas+1):
            x = int(input("Digite o elementro %i%i da matriz:" % (i,j)))
            naLinha.append(x)
            matriz.append(naLinha)

def somarMatriz (lin, colun, matriz):
    lin = linhas
    colun = colunas

    for i in range(linhas,):
        soma.append([])
        for j in range(colunas):
            x = linhas[i][j]+colunas[i][j]
            somarMatriz[i].append(x)

contrutorMatriz(linhas, colunas, matriz)
print(matriz)

print(somarMatriz)
