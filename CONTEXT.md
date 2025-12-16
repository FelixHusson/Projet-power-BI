Projet Analytique & MLOps — Contexte Complet
🎯 Objectif du projet
Ce projet a pour but de :

Développer un pipeline complet de Data Science  
Déployer un modèle de Machine Learning via une API FastAPI + Docker
Construire un dashboard Power BI
Organiser le tout dans une architecture propre et industrialisable

Ce fichier sert de contexte pour les LLM et pour documenter le projet.

🏗️ Architecture générale du repository
Projet-power-BI/
│
├── data/
│   ├── raw/                # Données brutes
│   ├── processed/          # Données nettoyées
│   └── datasets.py         # Script de génération/simulation de données
│
├── notebooks/
│   ├── 01_cleaning.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_training.ipynb
│
├── model/
│   └── model.pkl           # Modèle ML entraîné (pickle)
│
├── src/
│   ├── data_cleaning.py    # Nettoyage des données
│   ├── train_model.py      # Entraînement du modèle
│   └── api.py              # Code FastAPI
│
├── docker/
│   ├── Dockerfile          # Fichier Docker (valide)
│   └── requirements.txt    # Dépendances
│
├── powerbi/
│   └── dashboard.pbix      # Dashboard Power BI
│
├── README.md               # Présentation du projet
└── CONTEXT.md              # (ce fichier)

🧠 Pipeline Data Science
1. Nettoyage des données

Suppression des valeurs manquantes  
Encodage des variables catégorielles  
Normalisation

2. Feature Engineering

Construction de nouvelles variables explicatives  
Sélection de features importantes

3. Entraînement du modèle ML
Modèle typique :  

RandomForestClassifier  
XGBoost  
ou modèle de régression

Le résultat final est sauvegardé dans :
model/model.pkl

🚀 Service Web — API FastAPI
Le fichier d’API se trouve dans :
src/api.py
Endpoints principaux
GET /               → Health check
POST /predict       → Prédiction à partir d’un JSON
Exemple d’appel
POST /predict
{
  "age": 43,
  "income": 35000,
  "tenure": 5
}
Réponse :
{
  "prediction": 1,
  "confidence": 0.87
}

🐳 Déploiement avec Docker
Fichiers Docker
docker/
├── Dockerfile
└── requirements.txt
Contenu du Dockerfile (standard pour FastAPI)
FROM python:3.10

WORKDIR /app

COPY ../src ./src
COPY ../model ./model
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]

▶️ Commandes Docker
Depuis le dossier :
C:\Users\felix\PycharmProjects\Projet-power-BI\docker
Build
docker build -t churn-api .
Run
docker run -p 8000:8000 churn-api
API accessible sur :
http://localhost:8000/docs

📊 Dashboard Power BI
Le dossier powerbi/ contient :
dashboard.pbix
Contient :

KPI du modèle  
Performance (AUC, F1, confusion matrix)  
Profil client  
Analyse métier


🧱 Architecture Applicative (résumé)
Niveaux

Data Layer : data/raw, data/processed  
Machine Learning Layer : notebooks, src/train_model.py  
Model Serving Layer : FastAPI  
Containerization Layer : Docker  
BI Layer : Power BI

Flux général
raw data  
→ cleaning  
→ feature engineering  
→ model training  
→ model.pkl  
→ FastAPI service  
→ Docker container  
→ Power BI dashboard (consomme les données ou outputs)

📝 Notes techniques importantes

Le fichier Dockerfile est correctement nommé (pas Dockerfile.txt).  
Lors du build, il faut utiliser :

docker build -t churn-api .
depuis le dossier docker/.

Le modèle est chargé dans l’API via pickle.  
Le projet peut être étendu vers un déploiement Cloud (AWS, Azure).


🎯 Utilité de ce fichier
Ce fichier Markdown donne :

la structure complète du projet  
les détails du pipeline  
l’architecture logicielle  
les instructions Docker  
un résumé prêt à l’emploi pour tout LLM

