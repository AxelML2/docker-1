import os
import time

import pandas as pd


def clean_csv():
    ##############################
    # Sélection du fichier csv (raw)
    ##############################

    # On récupère tous les csv
    csv_filenames = [fn for fn in os.listdir() if fn.endswith(".csv")]
    # on les classe par ordre croissant
    csv_filenames = sorted(csv_filenames)
    # on prend le dernier élément
    filename = csv_filenames[-1]

    ##############################
    # cleaning du fichier csv
    ##############################

    #
    df = pd.read_csv(filename)

    # On supprime la colonne inutile
    df = df.drop("Unnamed: 0", axis=1)
    # On renomme les colonnes
    df.columns = ["rang", "title_fr", "title_vo", "réalisateur(s)", "année", "pays"]

    ##############################
    # Enregistrement
    ##############################

    filename_new = f"cleaned_{filename}"
    df.to_csv(filename_new)


while True:
    clean_csv()
    time.sleep(45)
