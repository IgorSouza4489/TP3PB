import multiprocessing
import math
import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def contar_primos_no_intervalo(inicio, fim):
    return sum(1 for i in range(inicio, fim) if is_prime(i))
def contar_primos_sequencialmente(inicio, fim):
    return sum(1 for i in range(inicio, fim) if is_prime(i))
def contar_primos_paralelamente(inicio, fim, num_processos=None):
    if num_processos is None:
        num_processos = multiprocessing.cpu_count() 
    tamanho = fim - inicio
    partes = [inicio + i * (tamanho // num_processos) for i in range(num_processos)] + [fim]
    with multiprocessing.Pool(processes=num_processos) as pool:
        resultados = pool.starmap(contar_primos_no_intervalo, [(partes[i], partes[i+1]) for i in range(num_processos)])
    return sum(resultados)

inicio, fim = 1, 100000
start_time = time.time()
quantidade_primos_sequencial = contar_primos_sequencialmente(inicio, fim)
end_time = time.time()
tempo_sequencial = end_time - start_time
start_time = time.time()
quantidade_primos_paralela = contar_primos_paralelamente(inicio, fim)
end_time = time.time()
tempo_paralelo = end_time - start_time
print(f"Quantidade de primos (sequencial): {quantidade_primos_sequencial} | Tempo: {tempo_sequencial:.6f} segundos")
print(f"Quantidade de primos (paralela): {quantidade_primos_paralela} | Tempo: {tempo_paralelo:.6f} segundos")
