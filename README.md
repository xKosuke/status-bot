# Status-Bot Kosuke

Bot discord en Python qui permet de faire du monitoring sur différentes adresses IP spécifiées et de choisir le port souhaité pour chaque adresse IP.

## Prérequis

- Python 3
- Asyncio ( ``pip install asyncio`` )
- Pytz ( ``pip install pytz`` )
- Ping3 ( ``pip install ping3`` )

## Utilisation

- Installez les différents modules
- Ouvrez le fichier ``bot.py`` dans un éditeur
- Mettre l'ID d'un salon discord ou le bot est présent ``ligne 13``
- Démarrer le bot, puis copier l'ID du message qu'il a envoyé dans le salon
- Mettre l'ID du message discord ``ligne 15``
- Mettre le token de votre bot discord à la ``ligne 42`` (Il est nécessaire d'activer les intents de votre bot Discord)
- Exécutez le script

## Configuration

- Vous pouvez configurer les différentes adresses IP que vous voulez afficher en respectant le format ``ligne 16``
- ``("HOSTNAME", PORT, "NAME")``
