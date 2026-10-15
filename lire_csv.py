import csv

CHEMIN = "data/prices.csv"
compte = 0

with open(CHEMIN, newline="", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier)
    for ligne in lecteur:
        if float(ligne["close"]) > 120:
            print(ligne["symbol"], ligne["close"])
            compte += 1
            if compte == 5:
                break