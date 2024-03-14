import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
import pandas as pd 
from code_propre import data_musique


load_dotenv() 
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="4d3bffd173c84f21ab47981ba6cd15f8", client_secret="fa770e1876084e4288c17530adf5423f"))

def recherche_piste(titre: str, artiste: str) -> str:
    """
    Recherche une piste Spotify en utilisant le titre et l'artiste.

    Parameters:
    - titre (str): Le titre de la piste.
    - artiste (str): Le nom de l'artiste.

    Returns:
    - str: L'URI de la première piste correspondante.
    """
    query = f"{titre} {artiste}"
    results = sp.search(query, type='track', limit=1)
    
    if results['tracks']['items']:
        return results['tracks']['items'][0]['uri']
    else:
        return ""

def obtenir_audio(uri: str) -> str:
    """
    Obtient l'URL de l'extrait audio à partir de l'URI d'une piste.

    Parameters:
    - uri (str): L'URI de la piste.

    Returns:
    - str: L'URL de l'extrait audio.
    """
    try:
        track_id = uri.split(":")[-1]
        track = sp.track(track_id)
        return track['preview_url']
    except spotipy.SpotifyException as e:
        print(f"Erreur Spotify lors de l'obtention de l'audio : {e}")
        return ""
    except requests.RequestException as e:
        print(f"Erreur de requête lors de l'obtention de l'audio : {e}")
        return ""
    except Exception as e:
        print(f"Erreur inattendue lors de l'obtention de l'audio : {e}")
        return ""


def renvoyer_piste_audio(titre: str, artiste: str) -> str:
    """
    Recherche une piste, obtient l'URI, puis récupère l'URL de l'extrait audio.

    Parameters:
    - titre (str): Le titre de la piste.
    - artiste (str): Le nom de l'artiste.

    Returns:
    - str: L'URL de l'extrait audio.
    """
    uri = recherche_piste(titre, artiste)

    if uri:
        url = obtenir_audio(uri)
        print(f"URL de l'extrait audio : {url}")
        return url
    else:
        print(f"Piste non trouvée pour {titre} de {artiste}")
        return ""


# Exemple avec une recherche de piste
titre_exemple = "Shape of You"
artiste_exemple= "Ed Sheeran"
renvoyer_piste_audio(titre_exemple,artiste_exemple)




# class SpotifyAPI:
#     def __init__(self):
#         self.sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

#     def recherche_piste(self, titre, artiste):
#         query = f"{titre} {artiste}"
#         results = self.sp.search(query, type='track', limit=1)
#         if results['tracks']['items']:
#             return results['tracks']['items'][0]['uri']
#         else:
#             return None

#     def obtenir_audio(self, uri):
#         track = self.sp.track(uri)
#         return track['preview_url']

#     def renvoyer_piste_audio(self, titre, artiste):
#         uri = self.recherche_piste(titre, artiste)

#         if uri:
#             url = self.obtenir_audio(uri)
#             print(url)
#             return url
#         else:
#             print(f"Piste non trouvée pour {titre} de {artiste}")
#             return None



# # Exemple avec une recherche de piste
# spotify_api = SpotifyAPI()
# titre = "Shape of You"
# artiste = "Ed Sheeran"
# spotify_api.renvoyer_piste_audio(titre, artiste)






table_carte = data_musique[['Date', 'Artiste', 'Titre']].copy()
table_carte['Audio'] = None


for index, row in table_carte.iterrows():
    titre = row['Titre']
    artiste = row['Artiste']

    
    print(f"Processing {titre} by {artiste}")

    
    audio_url = renvoyer_piste_audio(titre, artiste)
    print(f"Audio URL: {audio_url}")
    table_carte.loc[index, 'Audio'] = audio_url

table_carte.to_csv("table_carte.csv",sep=";")