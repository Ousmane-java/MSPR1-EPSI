# MSPR1-EPSI

# 🛡️ Seahawks Monitoring System

**Seahawks Monitoring** est une solution de **scan réseau automatisé**, avec **interface web intuitive**, serveur de réception distant, et envoi sécurisé des résultats d’analyse. Ce projet a été réalisé dans le cadre de ma formation en **Administration Systèmes et Réseaux** à l’EPSI Lyon.

> 📍 Objectif : Scanner automatiquement les machines sur un réseau local, détecter les ports ouverts et envoyer les résultats à un serveur central hébergé sur le Cloud.

---

## 🔧 Fonctionnalités

- 🔍 Scan réseau complet avec `nmap`
- 📡 Détection automatique du sous-réseau /24
- 🌐 Interface web responsive (Bootstrap 5)
- 🚀 Envoi automatique des données vers le serveur central
- 🐧 Script Bash d’automatisation des updates Git + dépendances
- ☁️ Serveur Cloud Dockerisé (Cloud Run)
- 📊 Visualisation des résultats en direct + export

---

## 📁 Structure du projet

```
├── harvester/              # Partie Client (Scan + Interface)
│   ├── app/
│   ├── run.py
│   └── ...
├── nester/                 # Partie Serveur (API + DB)
│   ├── app/
│   ├── Dockerfile
│   ├── run.py
│   └── ...
├── README.md
```

---

## 🚀 Installation et Lancement

### 1. Cloner le dépôt

```bash
git clone https://github.com/Ousmane-java/MSPR1-EPSI.git
cd MSPR1-EPSI
```

---

## ⚙️ Partie 1 : Lancer le **Client Harvester** (scan + dashboard)

### 🔹 Pré-requis

- Python 3.8+
- `nmap` installé sur votre machine (Linux/macOS : `sudo apt install nmap` ou `brew install nmap`)
- Virtualenv (optionnel)

### 🔹 Configuration

1. **Modifier l’adresse du serveur distant**

Dans `harvester/app/views/routes.py`, modifiez la variable contenant l’URL du serveur :

```python
NESTER_SERVER_URL = "https://mon-api-report-623064689779.europe-west1.run.app/api/report"  # c'est l'url de mon cloud vous pouvez aussi creer votre propre cloud et heberger le serveur 
```

2. **Créer un environnement virtuel et installer les dépendances :**

```bash
cd harvester
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **Lancer l’application**

```bash
python run.py
```

Puis accéder à : `http://localhost:5000`

> 🛠️ Le port est modifiable dans `run.py` (par défaut `5000`)

---

## 🌐 Partie 2 : Déployer le **Serveur Nester** (réception des données)

### 🔹 Prérequis

- Python 3.8+
- SQLite (inclus)
- `Flask`, `SQLAlchemy`, `gunicorn`
- Docker & Cloud Run (pour production)

### 🔹 Variables d’environnement

Créer un fichier `.env` ou définir dans l’environnement :

```env
SECRET_KEY=cle-secrete-de-dev
DATABASE_URL=sqlite:///db.sqlite3
```

### 🔹 Lancer en local (dev)

```bash
cd nester
python run.py
```

Accessible sur `http://localhost:8000` (modifiable dans `run.py`)

### 🔹 Déploiement Docker (optionnel)

```bash
cd nester
docker build -t nester-server .
docker run -d -p 8080:8080 nester-server
```

---

## ⚙️ Automatisation Bash (facultatif)

Dans le répertoire `harvester`, un script Bash permet :

- de vérifier automatiquement les mises à jour Git
- d’installer les nouvelles dépendances si nécessaire
- de lancer ensuite le scan proprement

```bash
chmod +x start.sh
./start.sh
```

---

## 📬 Envoi Automatique des données

L’envoi vers le serveur Nester est réalisé en JSON via `fetch("/send")` dans le frontend, POST vers `/report`.

Structure JSON envoyée :

```json
{
  "hostname": "Client-PC",
  "ip": "192.168.0.12",
  "latency": "Ping réussi (3ms)",
  "nb_machines": 5,
  "scan": [...],
  "version": "1.0.0"
}
```

---

## 🔐 Sécurité

- ✅ Communication via HTTPS (Cloud Run)
- ✅ Environnement Python isolé
- ✅ Scan sans privilèges root (`-sT` au lieu de `-sS`)
- ✅ Envoi uniquement depuis client autorisé

---

## 📌 À venir (perspectives)

- 🎫 Système de ticketing intégré (remontée incidents)
- 🔐 Authentification des Harvesters
- 🧠 Analyse automatisée des ports critiques
- 📈 Dashboard global pour l’administrateur réseau

---

## 👨‍💻 Auteur

**Ousmane Drame**  
🎓 Étudiant en Bachelor Systèmes & Réseaux à l’EPSI Lyon  
📬 ousmanedrame.edu@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/ousmane-drame-83858a334/)

---

## 📢 Licence

Projet open-source libre d’utilisation à des fins pédagogiques et professionnelles.  
© 2025 - Seahawks Monitoring Project