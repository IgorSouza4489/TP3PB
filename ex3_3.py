import multiprocessing

class TreeNode:
    def __init__(self, valor):
        self.valor = valor
        self.esquerdo = None
        self.direito = None
def busca_maxima_paralela(no, resultado):
    if no is None:
        return
    resultado.append(no.valor)
    processos = []
    if no.esquerdo:
        p_esquerdo = multiprocessing.Process(target=busca_maxima_paralela, args=(no.esquerdo, resultado))
        processos.append(p_esquerdo)
        p_esquerdo.start()
    if no.direito:
        p_direito = multiprocessing.Process(target=busca_maxima_paralela, args=(no.direito, resultado))
        processos.append(p_direito)
        p_direito.start()
    for p in processos:
        p.join()
def encontrar_valor_maximo(no):
    resultado = multiprocessing.Manager().list()  
    busca_maxima_paralela(no, resultado)
    return max(resultado) if resultado else None

raiz = TreeNode(15)
raiz.esquerdo = TreeNode(10)
raiz.direito = TreeNode(20)
raiz.esquerdo.esquerdo = TreeNode(8)
raiz.esquerdo.direito = TreeNode(12)
raiz.direito.esquerdo = TreeNode(17)
raiz.direito.direito = TreeNode(25)
valor_maximo = encontrar_valor_maximo(raiz)
print(f"O valioor máximo na árvore é: {valor_maximo}")
