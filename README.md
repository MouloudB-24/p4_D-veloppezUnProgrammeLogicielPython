# Application de Gestion des Tournois d'Échecs

## Introduction

Ceci est une application Python conçue pour gérer des tournois d'échecs hors ligne.
L'application permet de créer des joueurs, d'organiser des tournois, de générer des appariements de matchs et
d'enregistrer les résultats des matchs.

## Fonctionnalités

- Ajouter et gérer des joueurs avec des détails tels que le nom, la date de naissance, le sexe et l'ID national d'
  échecs.
- Créer et gérer des tournois avec des tours spécifiés.
- Générer des appariements de matchs pour chaque tour.
- Enregistrer et mettre à jour les résultats des matchs.
- Afficher les classements des joueurs et les détails des tournois.

## Installation

1. **Cloner le dépôt :**

   ```sh
   git clone clone git@github.com:MouloudB-24/p4_DeveloppezUnProgrammeLogicielPython.git
   ```
2. **Créer un environnement virtuel**
    ```sh
      python -m venv venv
      source venv/bin/activate  # Sous Windows utilisez `venv\Scripts\activate`
   ```
3. **Installer les dépendances**

```sh
   pip install -r requirements.txt
   ```

4. **Lancer l'application**

```sh
   python3 main.py
   ```

## Vérification de la Conformité du Code avec PEP 8

Pour vérifier la conformité du code avec les directives PEP 8 et générer un rapport HTML, suivez les étapes 
ci-dessous :

### Prérequis

Assurez-vous d'avoir `flake8` et `flake8-html` installés. Si ce n'est pas le cas, vous pouvez les installer en utilisant
la commande suivante :

```sh
   pip install flake8 flake8-html
   ```

### Générer le rapport
Pour générer un rapport HTML, exécutez la commande suivante à partir de la racine du projet :

```sh
   flake8 --format=html --htmldir=flake8_rapport
   ```

### Consulter le Rapport
Pour consulter le rapport, ouvrez le fichier index.html dans le répertoire flake8_rapport avec votre navigateur 
web préféré.
```sh
   open flake8_rapport/index.html
   ```
# ou sur Windows
```sh
   start flake8_rapport/index.html
   ```