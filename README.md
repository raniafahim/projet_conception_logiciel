# HITSTER - Le Quiz Musical Interactif

##  Présentation de HITSTER
#  A propos de Hitster

HITSTER est un jeu de quiz musical parfait pour tous ceux qui adorent la musique et les défis. Ce jeu teste non seulement vos connaissances des hits musicaux qui ont marqué l'histoire, mais stimule aussi votre sens de l'histoire musicale en vous invitant à organiser chronologiquement les titres découverts.

Enrichissant la version originale accessible sur [Hitster](https://hitstergame.com), notre adaptation propose spécialement des titres emblématiques français.


#  But du jeu 

À chaque tour, les joueurs scannent un QR code unique situé sur une carte, qui les redirige vers un extrait audio sur Spotify. Leur défi est de reconnaître non seulement le titre et l'artiste de la chanson jouée, mais aussi de déterminer l'année de sortie de la chanson. Une fois identifiées, les cartes doivent être placées dans l'ordre chronologique de leur date de sortie, créant ainsi une "timeline" musicale.

Le jeu se poursuit en boucle, chaque joueur ajoutant des cartes à la chronologie et en vérifiant la précision des positions avec les informations au dos des cartes. Celui qui positionne correctement le plus de cartes gagne la partie. C’est un moyen amusant et interactif d’en apprendre davantage sur les grands moments de la musique tout en s’amusant.



# Implémentation

Notre version de HITSTER tire parti de l'API Spotify pour générer une playlist interactive à partir de la liste des singles numéro un en France, comme référencé sur la page Wikipedia ([Liste des singles numéro un en France](https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France)). Le jeu génère ensuite un fichier PDF 'cartes_hitster' pour chaque morceau avec un QR code menant à l'extrait audio, et au verso, des détails sur la chanson.

## Débuter l'expérience HITSTER
# Installation des dépendances

Ce projet nécessite Python version 3.10.12 . Assurez-vous que Python est correctement installé sur votre système avant de continuer.

Pour installer toutes les dépendances requises pour ce projet, exécutez la commande suivante :

```bash
pip install -r requirements.txt     # installer tous les packages listés 
pip list                            # lister tous les packages installés
```

# Configuration du fichier .env

1. Ouvrez votre éditeur de texte ou IDE préféré et configurez vos clés d'API Spotify (client ID et client secret) dans un fichier .env. 
Pour cela, il vous faudra avoir un compte Spotify ou en créer un puis aller à l'adresse Spotify Developer Dashboard pour récupérer vos clés. 

2. Utilisez le modèle fourni pour s'assurer que vous remplissez correctement les informations nécessaires. Cela pourrait ressembler à ceci :

```bash

# .env
CLIENT_ID='votre_client_id_spotify_ici'
CLIENT_SECRET='votre_client_secret_spotify_ici'
``` 
3. Enregistrez les modifications apportées au fichier .env .


# Récupérez vos cartes 

1. Ouvrez un terminal ou une invite de commande et lancez le script principal avec la commande suivante :

```bash

python main.py
```

2. Une fois le script exécuté, un fichier PDF, nommé 'cartes_hitster', sera généré. Ce fichier contient les cartes. 
Localisez les fichiers PDF dans le dossier spécifié par votre script, imprimez-les, découpez les cartes, pliez les au milieu et votre jeu HITSTER est prêt à être utilisé !


Maintenant c'est à vous de jouer <3 


Auteurs : [Rania Fahim](https://github.com/raniafahim) et [Jean-Paul Younès](https://github.com/jpyns)
