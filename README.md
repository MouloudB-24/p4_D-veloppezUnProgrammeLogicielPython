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