════════════ ENGLISH ════════════

📊 Log Analyzer

A Python CLI tool for parsing and analyzing log files.

---

🎯 Objective

Develop a script capable of reading a log file and counting occurrences of predefined log levels (INFO, WARNING, ERROR, DEBUG, CRITICAL), regardless of their position or casing in the file.

---

⚙️ Features

- ✅ Read a file passed as a CLI argument
- ✅ Log level detection from a predefined set
- ✅ Case-insensitive normalization
- ✅ Occurrence counting with dictionaries
- ✅ Clean terminal output
- ✅ Basic error handling (missing args / invalid file)
- ✅ Message when no valid levels are found

---

🏗️ Project Structure
```
log-analyzer/
│
├── main.py       # Entry point
├── analyzer.py   # Log analysis logic
├── cli.py        # CLI argument handling
├── test.log      # Example log file
└── README.md
```

---

▶️ Usage
```bash
python3 main.py logfile.txt
```

Output example:
```
-----Résumé-----
INFO: 12
WARNING: 3
ERROR: 5
```

If no valid log levels are found:
```
Aucun niveau trouvé dans le fichier.
```

---

🧠 Technical Concepts

- File handling with context managers (`with open`)
- CLI argument handling with `sys.argv`
- Regular expressions (`re.findall`)
- Dictionary usage and dynamic counting
- Data normalization (string casing)
- Separation of concerns (CLI / logic / entry point)
- Basic defensive programming

---

🚀 Design Choices

- Log levels are defined explicitly to avoid counting unrelated uppercase words.
- Case normalization ensures robustness across different log formats.
- Modular structure allows future extensions (sorting, CSV export, JSON parsing, etc.).

---

📌 Future Improvements

- Sort output by frequency
- Export results to CSV
- JSON log format support
- Unit tests with pytest
- Improved CLI options with argparse

---

📈 Level

Beginner → Intermediate Python scripting project. Focus on clean structure, modularity, and robustness rather than complexity.

---



════════════ FRANÇAIS ════════════

📊 Log Analyzer

Un outil Python en ligne de commande pour analyser des fichiers de logs.

---

🎯 Objectif

Développer un script capable de lire un fichier log et de compter les occurrences des niveaux prédéfinis (INFO, WARNING, ERROR, DEBUG, CRITICAL), indépendamment de leur position ou casse dans le fichier.

---

⚙️ Fonctionnalités

- ✅ Lecture d'un fichier passé en argument
- ✅ Détection des niveaux basée sur un ensemble prédéfini
- ✅ Normalisation indépendante de la casse
- ✅ Comptage des occurrences via dictionnaires
- ✅ Affichage clair en terminal
- ✅ Gestion des erreurs basique (arguments manquants / fichier invalide)
- ✅ Message si aucun niveau valide n'est détecté

---

🏗️ Structure du Projet
```
log-analyzer/
│
├── main.py       # Point d'entrée
├── analyzer.py   # Logique d'analyse
├── cli.py        # Gestion des arguments
├── test.log      # Fichier de test
└── README.md
```

---

▶️ Utilisation
```bash
python3 main.py logfile.txt
```

Exemple de sortie :
```
-----Résumé-----
INFO: 12
WARNING: 3
ERROR: 5
```

Si aucun niveau valide n'est trouvé :
```
Aucun niveau trouvé dans le fichier.
```

---

🧠 Notions Techniques

- Manipulation de fichiers avec gestionnaires de contexte (`with open`)
- Gestion des arguments en ligne de commande avec `sys.argv`
- Expressions régulières (`re.findall`)
- Utilisation avancée des dictionnaires
- Normalisation des données texte
- Séparation des responsabilités (CLI / logique / point d'entrée)
- Programmation défensive simple

---

🚀 Choix de Conception

- Les niveaux sont définis explicitement afin d'éviter de compter des mots non pertinents.
- La normalisation garantit la robustesse face aux variations de casse.
- La structure modulaire permet des extensions futures.

---

📌 Améliorations Futures

- Tri des résultats par fréquence
- Export des résultats en CSV
- Support des logs au format JSON
- Tests unitaires avec pytest
- Options CLI enrichies avec argparse

---

📈 Niveau

Débutant → Intermédiaire — projet de scripting Python. L'accent est mis sur une structure propre, la modularité et la robustesse plutôt que sur la complexité.