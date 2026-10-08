import time

import requests

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


if __name__ == "__main__":
    page = recuperer_page()
    print("page recuperee :", len(page), "caracteres")
