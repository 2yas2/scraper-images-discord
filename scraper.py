import os
import random
import time
from urllib.parse import unquote

import requests
from bs4 import BeautifulSoup

URL = "https://commons.wikimedia.org/wiki/Commons:Explore/Pictures"
USER_AGENT = "ScraperImagesWikimedia/1.0 (projet etudiant; https://github.com/2yas2/scraper-images-discord)"
DELAI = 2
DOSSIER = "images"
HEADERS = {"User-Agent": USER_AGENT}


def telecharger(url):
    # on attend avant chaque requete pour ne pas surcharger le site
    time.sleep(DELAI)
    reponse = requests.get(url, headers=HEADERS, timeout=30)
    reponse.raise_for_status()
    return reponse


def recuperer_page(url=URL):
    return telecharger(url).text


def trouver_images(html):
    soupe = BeautifulSoup(html, "html.parser")
    liens = []
    for img in soupe.find_all("img"):
        src = img.get("src", "")
        if src.startswith("//"):
            src = "https:" + src
        if "upload.wikimedia.org/wikipedia/commons/" not in src:
            continue
        if src.lower().endswith((".jpg", ".jpeg", ".png")):
            liens.append(src)
    return liens


def choisir_image(html):
    liens = trouver_images(html)
    if not liens:
        return None
    return random.choice(liens)


def enregistrer_image(url):
    os.makedirs(DOSSIER, exist_ok=True)
    nom = unquote(url.split("/")[-1])
    chemin = os.path.join(DOSSIER, nom)
    with open(chemin, "wb") as fichier:
        fichier.write(telecharger(url).content)
    return chemin


def recuperer_image():
    page = recuperer_page()
    url = choisir_image(page)
    if url is None:
        print("aucune image trouvee sur la page")
        return None
    print("image choisie :", url)
    chemin = enregistrer_image(url)
    print("image enregistree :", chemin)
    return chemin


if __name__ == "__main__":
    recuperer_image()
