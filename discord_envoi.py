# partie discord : faite par un coequipier
import os

import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
SALON = os.getenv("DISCORD_CHANNEL_ID")
USER_AGENT = "DiscordBot (https://github.com/2yas2/scraper-images-discord, 1.0)"


def envoyer_image(chemin):
    if not TOKEN or not SALON:
        print("DISCORD_TOKEN ou DISCORD_CHANNEL_ID manquant dans le fichier .env")
        return False

    url = "https://discord.com/api/v10/channels/" + SALON + "/messages"
    headers = {"Authorization": "Bot " + TOKEN, "User-Agent": USER_AGENT}
    with open(chemin, "rb") as fichier:
        reponse = requests.post(url, headers=headers, files={"file": (os.path.basename(chemin), fichier)}, timeout=30)

    if reponse.status_code == 200:
        print("image envoyee sur discord")
        return True
    print("erreur discord :", reponse.status_code, reponse.text)
    return False
