import nmap
import socket

def guess_subnet():
    """
    Détermine le /24 à partir de l'IP locale.
    Exemple : si l'IP est 192.168.0.42, on renvoie '192.168.0.0/24'.
    """
    ip_local = socket.gethostbyname(socket.gethostname())  # Récupère l'IP locale
    octets = ip_local.split('.')  # ["192","168","0","42"]
    if len(octets) == 4:
        octets[3] = "0/24"        # On force le dernier octet à 0/24
        return '.'.join(octets)   # "192.168.0.0/24"
    else:
        # Si on ne peut pas parser, on met une valeur par défaut
        return "192.168.1.0/24"

def scan_network():
    """
    Scanne le réseau ET récupère les ports ouverts sur une plage donnée.
    Utilise un SYN scan (-sS) sur les 1000 ports les plus communs par exemple.
    """
    target_network = guess_subnet()
    scanner = nmap.PortScanner()
    
    # -sS = SYN scan, -p 1-1000 = ports 1 à 1000, -T4 = plus agressif/rapide
    scanner.scan(hosts=target_network, arguments='-sS -p 1-1000 -T4')
    results = []

    for host in scanner.all_hosts():
        host_state = scanner[host].state() if host in scanner.all_hosts() else "unknown"
        host_name = scanner[host].hostname() or "N/A"

        # Récupération des ports ouverts
        open_ports = []
        for proto in scanner[host].all_protocols():
            port_list = scanner[host][proto].keys()
            for port in port_list:
                port_state = scanner[host][proto][port]['state']
                if port_state == 'open':
                    open_ports.append(port)

        results.append({
            "host": host,
            "hostname": host_name,
            "state": host_state,
            "ports": open_ports
        })

    if not results:
        return [{
            "host": "Aucune machine détectée",
            "hostname": "",
            "state": "N/A",
            "ports": []
        }]
    return results
