#!/usr/bin/env python3
import requests

# URL du fichier CSV
CSV_URL = "https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv"

# Télécharge le fichier CSV à partir du lien et enregistre localement
def telecharger_csv():
    response = requests.get(CSV_URL)
    if response.status_code == 200:
        # Écrit le contenu dans un fichier CSV local
        with open("Popular_Baby_Names.csv", "w", newline="", encoding="utf-8") as csvfile:
            csvfile.write(response.text)
        print("Téléchargement et enregistrement du fichier CSV réussis.")
    else:
        print("Échec du téléchargement du fichier CSV.")

# Appel de la fonction de téléchargement
telecharger_csv()

