import nmap
import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    finally:
        s.close()

def guess_subnet():
    ip_local = get_local_ip()
    octets = ip_local.split('.')
    if len(octets) == 4:
        return f"{octets[0]}.{octets[1]}.{octets[2]}.0/24"
    return "192.168.1.0/24"

def scan_network():
    target_network = guess_subnet()
    scanner = nmap.PortScanner()
    scanner.scan(hosts=target_network, arguments='-sT -p 1-1000 -T4')
    
    results = []
    for host in scanner.all_hosts():
        state = scanner[host].state()
        hostname = scanner[host].hostname() or "N/A"
        open_ports = []

        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                if scanner[host][proto][port]['state'] == 'open':
                    open_ports.append(port)

        results.append({
            "host": host,
            "hostname": hostname,
            "state": state,
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
