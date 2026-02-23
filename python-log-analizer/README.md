📊 Log Analyzer
A Python CLI tool for parsing and analyzing log files.
Un outil Python en ligne de commande pour analyser des fichiers de logs.

---

🎯 Objective | Objectif
EN — Develop a script capable of reading a log file and counting occurrences of predefined log levels (INFO, WARNING, ERROR, DEBUG, CRITICAL), regardless of their position or casing in the file.
FR — Développer un script capable de lire un fichier log et de compter les occurrences des niveaux prédéfinis, indépendamment de leur position ou casse dans le fichier.

---

⚙️ Features | Fonctionnalités
✅ENFR✅Read a file passed as a CLI argumentLecture d'un fichier passé en argument✅Log level detection from a predefined setDétection des niveaux basée sur un ensemble prédéfini✅Case-insensitive normalizationNormalisation indépendante de la casse✅Occurrence counting with dictionariesComptage des occurrences via dictionnaires✅Clean terminal outputAffichage clair en terminal✅Basic error handling (missing args / invalid file)Gestion des erreurs basique✅Message when no valid levels are foundMessage si aucun niveau valide n'est détecté

---

🏗️ Project Structure | Structure du Projet
log-analyzer/
│
├── main.py        # Entry point / Point d'entrée
├── analyzer.py    # Log analysis logic / Logique d'analyse
├── cli.py         # CLI argument handling / Gestion des arguments
├── test.log       # Example log file / Fichier de test
└── README.md

---

▶️ Usage | Utilisation
bashpython3 main.py logfile.txt
Output example | Exemple de sortie :
-----Résumé-----
INFO: 12
WARNING: 3
ERROR: 5
If no valid log levels are found | Si aucun niveau valide n'est trouvé :
Aucun niveau trouvé dans le fichier.

---

🧠 Technical Concepts | Notions Techniques
EN — Concepts practiced throughout this project:

File handling with context managers (with open)
CLI argument handling with sys.argv
Regular expressions (re.findall)
Dictionary usage and dynamic counting
Data normalization (string casing)
Separation of concerns (CLI / logic / entry point)
Basic defensive programming

FR — Notions travaillées tout au long du projet :

Manipulation de fichiers avec gestionnaires de contexte (with open)
Gestion des arguments en ligne de commande avec sys.argv
Expressions régulières (re.findall)
Utilisation avancée des dictionnaires
Normalisation des données texte
Séparation des responsabilités (CLI / logique / point d'entrée)
Programmation défensive simple

---

🚀 Design Choices | Choix de Conception
EN

Log levels are defined explicitly to avoid counting unrelated uppercase words.
Case normalization ensures robustness across different log formats.
Modular structure allows future extensions (sorting, CSV export, JSON parsing, etc.).

FR

Les niveaux sont définis explicitement afin d'éviter de compter des mots non pertinents.
La normalisation garantit la robustesse face aux variations de casse.
La structure modulaire permet des extensions futures.

---

📌 Future Improvements | Améliorations Futures

 Sort output by frequency | Tri des résultats par fréquence
 Export results to CSV | Export des résultats en CSV
 JSON log format support | Support des logs au format JSON
 Unit tests with pytest | Tests unitaires avec pytest
 Improved CLI options with argparse | Options CLI enrichies avec argparse

---

📈 Level | Niveau
Beginner → Intermediate Python scripting project.
Focus on clean structure, modularity, and robustness rather than complexity.
Débutant → Intermédiaire — projet de scripting Python.
L'accent est mis sur une structure propre, la modularité et la robustesse plutôt que sur la complexité.