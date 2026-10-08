# Scraper d'images avec envoi sur Discord

Programme Python qui récupère une image sur la page Wikimedia Commons « Explore/Pictures » (https://commons.wikimedia.org/wiki/Commons:Explore/Pictures), l'enregistre dans le dossier `images/` (la miniature affichée sur la page), puis l'envoie sur un salon Discord.

Projet personnel réalisé seul, en dehors des cours. La partie Discord (discord_envoi.py) n'a pas été écrite par moi.

## Technos

- Python
- requests et BeautifulSoup pour le scraping
- python-dotenv pour lire le fichier `.env`
- API REST de Discord (envoi avec un bot)

## Lancer le projet

1. Installer les dépendances :

```
pip install -r requirements.txt
```

2. Copier `.env.example` en `.env` et remplir `DISCORD_TOKEN` (token du bot) et `DISCORD_CHANNEL_ID` (identifiant du salon). Le token ne doit jamais être écrit dans le code.
3. Lancer :

```
python main.py
```

Pour seulement récupérer l'image sans l'envoyer sur Discord : `python scraper.py`.

Le scraper attend 2 secondes avant chaque requête et se présente avec un User-Agent qui indique le nom du projet et son adresse.

## Partie Discord

La partie Discord (`discord_envoi.py`) n'a pas été écrite par moi. Elle est dans un fichier à part.

## Ce que j'ai fait

- le scraper (`scraper.py`) : récupération de la page, choix d'une image, enregistrement en local
- `main.py`, qui enchaîne le scraper puis l'envoi
