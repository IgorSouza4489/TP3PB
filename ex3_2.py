import multiprocessing

class TreeNode:
    def __init__(self, valor):
        self.valor = valor
        self.esquerdo = None
        self.direito = None
def busca_em_profundidade_paralela(no, alvo, caminho, resultado):
    if no is None:
        return
    caminho.append(no.valor)
    if no.valor == alvo:
        resultado.append(list(caminho))
        return
    processos = []
    if no.esquerdo:
        p_esquerdo = multiprocessing.Process(target=busca_em_profundidade_paralela, args=(no.esquerdo, alvo, caminho, resultado))
        processos.append(p_esquerdo)
        p_esquerdo.start()

    if no.direito:
        p_direito = multiprocessing.Process(target=busca_em_profundidade_paralela, args=(no.direito, alvo, caminho, resultado))
        processos.append(p_direito)
        p_direito.start()
    for p in processos:
        p.join()
    caminho.pop()
def dfs_paralela(no, alvo):
    resultado = multiprocessing.Manager().list()  
    busca_em_profundidade_paralela(no, alvo, [], resultado)
    return list(resultado)

raiz = TreeNode(1)
raiz.esquerdo = TreeNode(2)
raiz.direito = TreeNode(3)
raiz.esquerdo.esquerdo = TreeNode(4)
raiz.esquerdo.direito = TreeNode(5)
raiz.direito.esquerdo = TreeNode(6)
raiz.direito.direito = TreeNode(7)
caminho = dfs_paralela(raiz, 5)
print("Caminh encontrado:", caminho)
