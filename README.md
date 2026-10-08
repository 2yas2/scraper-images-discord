# Scraper d'images avec envoi sur Discord

Programme Python qui récupère une image sur la page Wikimedia Commons « Explore/Pictures » (https://commons.wikimedia.org/wiki/Commons:Explore/Pictures), l'enregistre dans le dossier `images/`, puis l'envoie sur un salon Discord.

Projet réalisé en [À COMPLÉTER : L1 ou L2], [À COMPLÉTER : année]. Le code source d'origine a été perdu, ce dépôt est une réécriture faite en 2026 à partir de la description du projet.

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

La partie Discord (`discord_envoi.py`) a été réalisée par un coéquipier : [À COMPLÉTER : nom du coéquipier]. Elle est dans un fichier à part et n'est pas de moi. Comme le code d'origine est perdu, ce fichier a lui aussi été réécrit pour ce dépôt.

## Captures d'écran

[À COMPLÉTER]

## Ce que j'ai fait

- le scraper (`scraper.py`) : récupération de la page, choix d'une image, enregistrement en local
- `main.py`, qui enchaîne le scraper puis l'envoi

[À COMPLÉTER : vérifier que cette liste correspond à ma part réelle]
