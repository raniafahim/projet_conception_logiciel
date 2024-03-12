
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import client_id, client_secret



sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))


def recherche_piste(titre, artiste):
    query = f"{titre} {artiste}"
    results = sp.search(query, type='track', limit=1)
    if results['tracks']['items'] : 
        return results['tracks']['items'][0]['uri']
    else:
        None


def obtenir_audio(uri):
    track = sp.track(uri)
    return track['preview_url']


# Méthode pour lancer une recherche Spotify et récupérer l'extrait audio

def renvoyer_piste_audio(titre, artiste):
    uri = recherche_piste(titre, artiste)

    if uri:
        url = obtenir_audio(uri)
        print(url)
        return url
    else:
        print(f"Piste non trouvée pour {titre} de {artiste}")
        return None


# Exemple avec une recherche de piste
titre = "Shape of You"
artiste = "Ed Sheeran"
renvoyer_piste_audio(titre,artiste)




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






