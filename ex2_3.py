import multiprocessing
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def contar_primos_no_intervalo(inicio, fim):
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
quantidade_primos = contar_primos_paralelamente(inicio, fim)
print(f"Quantidade de números primos entre {inicio} e {fim}: {quantidade_primos}")
