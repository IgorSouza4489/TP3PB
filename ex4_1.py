import ipaddress

def verificar_ip_no_prefixo(ip, prefixo):
    try:
        ip_obj = ipaddress.ip_address(ip)
        rede_obj = ipaddress.ip_network(prefixo, strict=False)
        return ip_obj in rede_obj
    except ValueError:
        return False  

ip = "192.168.1.5"
prefixo = "192.168.1.0/24"
resultado = verificar_ip_no_prefixo(ip, prefixo)
print(f"O IP {ip} está dentro do prefixo {prefixo}? {resultado}")
