import ipaddress

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_prefix = False
class IPv6Trie:
    def __init__(self):
        self.root = TrieNode()

    def _ip_to_binary(self, ip):
        ip_obj = ipaddress.ip_address(ip)
        return bin(int(ip_obj))[2:].zfill(128) 
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
trie = IPv6Trie()
prefixos = ["2001:db8::/32", "2001:db8:1234::/48"]
for prefixo in prefixos:
    trie.insert(prefixo)
ip_test = "2001:db8:1234:5678::1"
prefixo_encontrado = trie.longest_prefix_match(ip_test)
print(f"O prefixo mais específico para o IP {ip_test} é: {prefixo_encontrado}")
