from discord_envoi import envoyer_image
from scraper import recuperer_image

chemin = recuperer_image()
if chemin is not None:
    envoyer_image(chemin)
