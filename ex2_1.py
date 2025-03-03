import multiprocessing

def soma_parcial(numeros):
    return sum(numeros)
def soma_paralela(lista, num_processos=None):
    if num_processos is None:
        num_processos = multiprocessing.cpu_count()  
    tamanho = len(lista)
    partes = [lista[i::num_processos] for i in range(num_processos)] 
    with multiprocessing.Pool(processes=num_processos) as pool:
        resultados = pool.map(soma_parcial, partes)  
    return sum(resultados) 

lista_grande = list(range(1, 10_000_001))
soma_total = soma_paralela(lista_grande)
print("Soma total:", soma_total) 
