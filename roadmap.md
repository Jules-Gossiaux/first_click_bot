# Click bot

## Objectif final
Savoir coder un click bot qui joue à un jeu clicker (https://www.snokido.fr/jeu/businessman-simulator)

1. Il doit clicker sur cookie
    - Trouver position cookie et lui dire de clicker  Point(x=-1634, y=492)

2. Il doit maméliorer de haut en bas les items
    - Tous les 20 clicks, il doit aller voir si il peut acheter des items   
        - Il se dirige vers la position la plus basse de la boutique
        - Boucle
            - Si couleur = ...: alors click
            - Sinon monter d'une case
            - Si couleur = Noir/brun: Sortir de boucle et clicker
