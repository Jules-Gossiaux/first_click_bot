# First Click Bot

Un bot automatisé pour jouer au jeu clicker "Businessman Simulator" en utilisant Python et PyAutoGUI.

## Description

Ce projet est un bot automatique qui :
- Clique automatiquement sur le cookie principal
- Améliore automatiquement les items de haut en bas dans la boutique
- Utilise la détection de couleur pour identifier les éléments cliquables

## Fichiers du projet

- `main.py` - Script principal du bot
- `get_position.py` - Utilitaire pour obtenir la position du curseur
- `get_colour.py` - Utilitaire pour obtenir la couleur d'un pixel
- `get_height.py` - Utilitaire pour calculer la hauteur des éléments
- `commandes.ipynb` - Notebook Jupyter avec les commandes de test
- `roadmap.md` - Plan de développement du projet

## Prérequis

- Python 3.x
- PyAutoGUI

## Installation

1. Clonez ce repository :
```bash
git clone https://github.com/Jules-Gossiaux/first_click_bot.git
cd first_click_bot
```

2. Installez les dépendances :
```bash
pip install pyautogui
```

## Utilisation

1. Ouvrez le jeu [Businessman Simulator](https://www.snokido.fr/jeu/businessman-simulator)
2. Ajustez les coordonnées dans `main.py` si nécessaire
3. Lancez le bot :
```bash
python main.py
```

## Configuration

Vous pouvez modifier les paramètres suivants dans `main.py` :
- `initial_pos` : Position initiale du curseur
- `item_height` : Hauteur entre les items
- `colour_items` : Couleurs des items détectables

## Avertissement

Ce bot est créé à des fins éducatives. Assurez-vous de respecter les conditions d'utilisation des jeux sur lesquels vous l'utilisez.

## Auteur

Jules Gossiaux
