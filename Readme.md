# Prédiction de l’état d’une valve hydraulique  
Projet Machine Learning — Classification binaire  

---

## Objectif du projet

L’objectif est de prédire l’état d’une **valve hydraulique**  
(optimale ou non optimale) à partir de mesures issues de capteurs
industriels.

Chaque ligne du dataset final correspond à **un cycle complet de
fonctionnement** de la valve.

La cible est issue du fichier `profile.txt` :
- valve optimale → 1  
- valve non optimale → 0  
## Description des fichiers capteurs

| Capteur | Mesure | Impact d’une valve défectueuse |
|--------|--------|--------------------------------|
| VS1 | Vibrations |  vibrations dues aux frottements |
| PS1–PS6 | Pressions | Pression instable, chutes |
| FS1–FS2 | Débits | Débit réduit ou irrégulier |
| TS1–TS4 | Températures |  température due à la friction |
| EPS1 | Efficacité pompe | Baisse d’efficacité |
| CE | Consommation énergie | Surconsommation |
| CP | Pression de contrôle | Mauvaise régulation |
| SE | Énergie système | Déséquilibre global |

Chaque fichier contient :
- 2205 lignes = 2205 cycles  
- chaque ligne = un cycle  
- chaque colonne = un instant temporel dans le cycle

## Où se trouvent les données ?

Toutes les données brutes et intermédiaires se trouvent dans le dossier `data/` :

- Les fichiers `.txt` contiennent les signaux bruts par cycle  
- `profile.txt` contient l’état réel de la valve  
- `dataset_final.csv` est le dataset utilisé pour l’entraînement  
- `dataset_streamlit.csv` est le dataset utilisé par l’application web  

---

## Où se trouvent les scripts ?

Tous les scripts de traitement, de feature engineering et d’entraînement
se trouvent dans le dossier `src/` :

- `PS1_script.ipynb`  
  → Analyse des données ps1 et extraction de features les plus utiles

- `PSI_script.ipynb`  
  → Analyse des données de PS2 jusqu'a PS6 et extraction des statistiques par cycle  pour la pression  

- `VS1_script.ipynb`  
  → Analyse des données de VS1 et extraction de features les plus utiles

- `EPS1_script.ipynb`  
  → Analyse des données de EPS1 et extraction de features les plus utiles

- `FS_script.ipynb`  
  → Analyse des données des deux fihcier FS1 et FS2 et extraction de features les plus utiles

- `TS_script.ipynb`  
  → Analyse des données des quatre fihcier TS1-TS4 et extraction de features les plus utiles

- `feature_engineering.py`  
  → extraction des statistiques par cycle  

- `Random_forest.ipynb`  
  → entrainement du model Random forest

- `Regression_logistic.ipynb`  
  → entrainement du model Regression logistic

- `SVM.ipynb`  
  → entrainement du model SVM

- `KNN.ipynb`  
  → entrainement du model KNN 

- `dataset_final.csv`  
  → c'est notre dataset_final avec toutes features extraite

- `app.py`  
  → notre fichier pour l'interface streamlit

- `dataset_streamlit.csv`  
  → dataset utilisé pour la demo de notre interface pour la prediction

- `svm_model.pkl`  
  → notre model svm qui a était utilisé pour notre interface

###  Prérequis

L’utilisateur doit uniquement avoir :

- Docker installé  
  👉 https://www.docker.com/products/docker-desktop  

---

### Lancer le projet avec Docker

Depuis la racine du projet (là où se trouve le fichier `Dockerfile`) :

```bash
docker build -t valve-ml-app .
docker run -p 8501:8501 valve-ml-app

### 4️⃣ Lancer l’application Streamlit (sans Docker – optionnel)

Si l’utilisateur souhaite lancer directement l’application web sans passer par Docker :

```bash
streamlit run app.py
puis lancer dans un navigateur : http://localhost:8501

Exécuter les tests unitaires

Pour vérifier la validité du feature engineering et des modèles :

pytest tests/




