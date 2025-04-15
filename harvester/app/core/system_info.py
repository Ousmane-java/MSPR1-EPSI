import socket
import subprocess
import re
import platform

def get_ip_hostname():
    hostname = socket.gethostname()
    try:
        ip = socket.gethostbyname(hostname)
    except:
        ip = "Inconnu"
    return ip, hostname

def get_latency(target="8.8.8.8"):
    """
    Mesure de la latence avec compatibilité multiplateforme (Windows, macOS, Linux).
    """
    system = platform.system()
    
    if system == "Windows":
        cmd = ["ping", "-n", "4", target]
        regex = r"Moyenne = (\d+)"
    else:
        cmd = ["ping", "-c", "4", target]
        regex = r"time=(\d+\.\d+)"

    try:
        output = subprocess.run(cmd, capture_output=True, text=True)
        if output.returncode != 0:
            return "Ping échoué"

        match = re.findall(regex, output.stdout)
        if match:
            # Convertir toutes les valeurs en float et calculer la moyenne
            values = [float(val) for val in match]
            avg = sum(values) / len(values)
            return f"{round(avg, 2)} ms (moyenne)"
        else:
            return "Impossible de déterminer la latence."
    except Exception as e:
        return f"Erreur: {str(e)}"
