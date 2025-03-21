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
    Scanne automatiquement le sous-réseau déterminé par guess_subnet().
    Utilise un 'ping scan' (-sn) pour détecter les hôtes allumés.
    """
    target_network = guess_subnet()
    scanner = nmap.PortScanner()
    scanner.scan(hosts=target_network, arguments='-sn')
    results = []

    for host in scanner.all_hosts():
        results.append({
            "host": host,
            "hostname": scanner[host].hostname() or "N/A",
            "state": scanner[host].state() or "unknown"
        })

    if not results:
        # Aucun hôte trouvé (peut-être bloqué par firewall)
        return [{
            "host": "Aucune machine détectée",
            "hostname": "",
            "state": "N/A"
        }]
    return results
