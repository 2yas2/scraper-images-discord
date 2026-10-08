import random
import time

import requests
from bs4 import BeautifulSoup

URL = "https://commons.wikimedia.org/wiki/Commons:Explore/Pictures"
USER_AGENT = "ScraperImagesWikimedia/1.0 (projet etudiant; https://github.com/2yas2/scraper-images-discord)"
DELAI = 2
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


if __name__ == "__main__":
    page = recuperer_page()
    print("page recuperee :", len(page), "caracteres")
    print("image choisie :", choisir_image(page))
