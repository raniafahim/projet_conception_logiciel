
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '342220e2c9f9455c873255aa5d775585'
client_secret = '270abe3660bf4562b1e9941ca01acbb5'

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





