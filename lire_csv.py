import csv

CHEMIN = "data/prices.csv"

with open(CHEMIN, newline="", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier)
    for i, ligne in enumerate(lecteur):
        print(ligne)
        if i == 4:
            break