import subprocess

# 1. Nettoyage R
subprocess.run(["Rscript", "scripts/data_cleaning.R"])

# 2. Ré-entraînement modèle Python
subprocess.run(["python", "churn_model.py"])

