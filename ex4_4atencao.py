import ipaddress
import time

def buscar_linear(prefixos, ip):
    ip_obj = ipaddress.ip_address(ip)
    for prefixo in prefixos:
        if ip_obj in ipaddress.ip_network(prefixo):
            return prefixo
    return None

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_prefix = False
class IPv4Trie:
    def __init__(self):
        self.root = TrieNode()
    def _ip_to_binary(self, ip):
        ip_obj = ipaddress.ip_address(ip)
        return bin(int(ip_obj))[2:].zfill(32)  
    def insert(self, prefix):
        network = ipaddress.ip_network(prefix, strict=False)
        binary_prefix = self._ip_to_binary(str(network.network_address))[:network.prefixlen]

        node = self.root
        for bit in binary_prefix:
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        node.is_end_of_prefix = True
    def longest_prefix_match(self, ip):
        binary_ip = self._ip_to_binary(ip)
        node = self.root
        match = ""
        
        for bit in binary_ip:
            if bit in node.children:
                node = node.children[bit]
                match += bit
                if node.is_end_of_prefix:
                    longest_match = match
            else:
                break
        if match:
            return ipaddress.ip_network(f"{ipaddress.ip_address(int(longest_match, 2))}/{len(longest_match)}", strict=False)
        else:
            return None

def comparar_desempenho(prefixos, ip):
    start_time = time.time()
    resultado_linear = buscar_linear(prefixos, ip)
    tempo_linear = time.time() - start_time
    trie = IPv4Trie()
    for prefixo in prefixos:
        trie.insert(prefixo)
    start_time = time.time()
    resultado_trie = trie.longest_prefix_match(ip)
    tempo_trie = time.time() - start_time
    print(f"Resultado da busca linear: {resultado_linear}")
    print(f"Tempo de execução da busca linear: {tempo_linear:.6f} segundos")
    print(f"Resultado da busca usando Trie: {resultado_trie}")
    print(f"Tempo de execução da busca usando Trie: {tempo_trie:.6f} segundos")
prefixos = [f"192.168.1.{i}/24" for i in range(1, 1001)]
ip_test = "192.168.1.55"

comparar_desempenho(prefixos, ip_test)
