import multiprocessing

def multiplicar_linha(matriz_a, matriz_b, linha_idx, resultado):
    resultado_linha = []
    for j in range(len(matriz_b[0])):
        valor = sum(matriz_a[linha_idx][k] * matriz_b[k][j] for k in range(len(matriz_a[0])))
        resultado_linha.append(valor)
    resultado[linha_idx] = resultado_linha
def multiplicar_matrizes(matriz_a, matriz_b):
    linhas_resultado = len(matriz_a)
    resultado = multiprocessing.Manager().list([None] * linhas_resultado)
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.starmap(multiplicar_linha, [(matriz_a, matriz_b, i, resultado) for i in range(linhas_resultado)])
    return [list(linha) for linha in resultado]
matriz_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriz_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
matriz_resultante = multiplicar_matrizes(matriz_a, matriz_b)
for linha in matriz_resultante:
    print(linha)
