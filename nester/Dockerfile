FROM python:3.12-slim

# Installer nmap et les dépendances système
RUN apt-get update && apt-get install -y nmap gcc libffi-dev libssl-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copier les fichiers de l'application
WORKDIR /app
COPY . .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port Flask
EXPOSE 8080

# Démarrer l’application
CMD ["python", "run.py"]