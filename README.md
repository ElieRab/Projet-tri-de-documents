📄 Projet de tri automatique de documents (CV / Annonces)

Ce projet a pour objectif de classer automatiquement des documents PDF et DOCX en deux catégories :

CV

Annonces

La classification repose sur l’analyse du texte des documents et l’identification de mots-clés caractéristiques de chaque catégorie.
Les fichiers sont ensuite automatiquement déplacés vers le dossier correspondant.

🚀 Fonctionnalités

✔️ Parcours automatique d’un dossier contenant des PDF et des fichiers Word

✔️ Extraction de texte :

PyPDF2 pour les PDF

python-docx pour les .docx

✔️ Détection intelligente basée sur un score de mots-clés

✔️ Tri automatique des fichiers dans :

/CV/

/Annonces/

✔️ Gestion des accents et nettoyage du texte

🧠 Comment ça marche ?

Le script parcourt tous les fichiers d’un dossier source.

Pour chaque document, il extrait le texte.

Il calcule deux scores :

un score CV

un score Annonce

Selon le score le plus élevé, le document est déplacé dans le dossier correspondant.

Ce système simple mais efficace permet de trier rapidement de grands volumes de documents.

🛠️ Technologies utilisées

Python 3

PyPDF2

python-docx

pathlib

shutil

re

📁 Structure du projet
Projet-tri-documents/
│
├── Projet tri documents git.ipynb      # Notebook principal
├── data/                                # Dossier avec vos documents à trier
├── CV/                                  # Dossier de sortie pour les CV
└── Annonces/                            # Dossier de sortie pour les annonces

▶️ Exécution

Clonez le dépôt

git clone https://github.com/ElieRab/Projet-tri-de-documents.git


Installez les dépendances

pip install PyPDF2 python-docx


Lancez le script (ou le notebook)

Ouvrir le notebook et exécuter les cellules.

📌 Améliorations possibles

Ajouter un modèle de machine learning (Naive Bayes, Logistic Regression…)

Gérer plus de catégories de documents

Améliorer l’extraction de texte PDF (utiliser pdfminer.six)

Construire une interface utilisateur (Tkinter, Streamlit)

📄 Licence

Projet libre d’utilisation dans un cadre personnel ou académique.
