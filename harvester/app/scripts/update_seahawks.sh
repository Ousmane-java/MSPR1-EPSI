#!/bin/bash
#Configuration personnalisée pour la machine
PROJECT_DIR="C:\Users\intel\Downloads\MSPR OU\MSPR1-EPSI"
GIT_REPO_URL="git@gitlab.com:zaf223/seahawks-harvester.git"
BRANCH="main"
VIRTUAL_ENV_DIR="C:\Users\intel\Downloads\MSPR OU\MSPR1-EPSI\harvester\venv"

# Vérifier l'existence du répertoire du projet
if [ -d "$PROJECT_DIR" ]; then
  cd "$PROJECT_DIR"
else
  echo "Le répertoire $PROJECT_DIR n'existe pas."
  exit 1
fi

# Vérifier si le dépôt Git existe déjà
if [ -d ".git" ]; then
  echo "Dépôt Git trouvé. Mise à jour..."
  git pull origin $BRANCH
else
  echo "Dépôt Git non trouvé. Clonage du dépôt..."
  git clone $GIT_REPO_URL .
  git checkout $BRANCH
fi

# Mettre à jour les dépendances
if [ -d "$VIRTUAL_ENV_DIR" ]; then
  echo "Activation de l'environnement virtuel..."
  source "$VIRTUAL_ENV_DIR/Scripts/activate"
else
  echo "Environnement virtuel non trouvé. Création de l'environnement virtuel..."
  python -m venv "$VIRTUAL_ENV_DIR"
  source "$VIRTUAL_ENV_DIR/Scripts/activate"
fi

echo "Mise à jour des dépendances..."
pip install -r requirements.txt

# Redémarrage de l'application
echo "Redémarrage de l'application..."
# pkill -f flask
# python run.py &

echo "✅ Mise à jour terminée avec succès !"