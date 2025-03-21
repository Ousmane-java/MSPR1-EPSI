import socket
import subprocess
import re

def get_ip_hostname():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip, hostname

def get_latency(target="8.8.8.8"):
    """
    Sous Windows, on utilise 'ping -n 4'.
    On parse la ligne 'Minimum = Xms, Maximum = Yms, Moyenne = Zms'.
    """
    try:
        output = subprocess.run(["ping", "-n", "4", target],
                                capture_output=True, text=True)
        if output.returncode != 0:
            return "Ping échoué"

        match = re.search(r"Minimum = (\d+)ms, Maximum = (\d+)ms, Moyenne = (\d+)ms", output.stdout)
        if match:
            _, _, avg_ms = match.groups()
            return f"{avg_ms} ms (moyenne)"
        else:
            return "Impossible de déterminer la latence."
    except Exception as e:
        return f"Erreur: {str(e)}"