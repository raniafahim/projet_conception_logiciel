import unittest
from unittest.mock import MagicMock, patch
#from api.py import SpotifyAPI  

# class TestSpotifyAPI(unittest.TestCase):
#     def setUp(self):
#         self.spotify_api = SpotifyAPI()

#     @patch('spotipy.Spotify.search')
#     def test_recherche_piste(self, mock_search):
#         # Mock de la réponse de l'API Spotify
#         mock_search.return_value = {'tracks': {'items': [{'uri': 'mocked_uri'}]}}

#         # Test de la méthode recherche_piste
#         uri = self.spotify_api.recherche_piste('MockedTitle', 'MockedArtist')
#         self.assertEqual(uri, 'mocked_uri')

#     @patch('spotipy.Spotify.track')
#     def test_obtenir_audio(self, mock_track):
#         # Mock de la réponse de l'API Spotify
#         mock_track.return_value = {'preview_url': 'mocked_url'}

#         # Test de la méthode obtenir_audio
#         url = self.spotify_api.obtenir_audio('mocked_uri')
#         self.assertEqual(url, 'mocked_url')

#     @patch('spotify_api_module.SpotifyAPI.recherche_piste')
#     @patch('spotify_api_module.SpotifyAPI.obtenir_audio')
#     def test_renvoyer_piste_audio(self, mock_obtenir_audio, mock_recherche_piste):
#         # Mock des méthodes internes
#         mock_recherche_piste.return_value = 'mocked_uri'
#         mock_obtenir_audio.return_value = 'mocked_url'

#         # Test de la méthode renvoyer_piste_audio
#         url = self.spotify_api.renvoyer_piste_audio('MockedTitle', 'MockedArtist')
#         self.assertEqual(url, 'mocked_url')

#     @patch('spotify_api_module.SpotifyAPI.recherche_piste')
#     def test_renvoyer_piste_audio_not_found(self, mock_recherche_piste):
#         # Mock de la méthode recherche_piste pour simuler un résultat non trouvé
#         mock_recherche_piste.return_value = None

#         # Test de la méthode renvoyer_piste_audio pour le cas où la piste n'est pas trouvée
#         url = self.spotify_api.renvoyer_piste_audio('NonExistentTitle', 'NonExistentArtist')
#         self.assertIsNone(url)

# if __name__ == '__main__':
#     unittest.main()




import unittest
from unittest.mock import patch, MagicMock
from api import SpotifyApi 

class TestSpotifyApi(unittest.TestCase):
    def setUp(self):
        self.finder = SpotifyApi()

    @patch('api.spotipy.Spotify.search')
    def test_recherche_piste_trouvee(self, mock_search):
        mock_search.return_value = {'tracks': {'items': [{'uri': 'spotify:track:123'}]}}
        uri = self.finder.recherche_piste('titre', 'artiste')
        self.assertEqual(uri, 'spotify:track:123')

    @patch('api.Spotify.search')
    def test_recherche_piste_non_trouvee(self, mock_search):
        mock_search.return_value = {'tracks': {'items': []}}
        uri = self.finder.recherche_piste('titre', 'artiste')
        self.assertEqual(uri, '')

    @patch('api.Spotify.track')
    def test_obtenir_audio(self, mock_track):
        mock_track.return_value = {'preview_url': 'https://exemple.com/preview.mp3'}
        url = self.finder.obtenir_audio('spotify:track:123')
        self.assertEqual(url, 'https://exemple.com/preview.mp3')

    

if __name__ == '__main__':
    unittest.main()



import unittest
from unittest.mock import MagicMock, patch
from scrapping import WikipediaScraper  


class TestWikipediaScraper(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.url = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"
        self.target_date = "4/11/1984"
        self.file_path = "test_musique.csv"
        self.scraper = WikipediaScraper(self.url)

    def test_scrape_data(self):
        self.scraper.scrape_data(self.target_date)
        self.assertTrue(len(self.scraper.data) > 0, "Aucune donnée scrapée")


    def test_save_to_csv(self):
        self.scraper.save_to_csv(self.file_path)
        self.assertTrue(os.path.exists(self.file_path), "Le fichier CSV n'a pas été créé")

    def test_create_dataframe(self):
        df = self.scraper.create_dataframe()
        self.assertIsNotNone(df, "Le dataframe n'a pas été créé")


    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.file_path):
            os.remove(cls.file_path)

if __name__ == '__main__':
    unittest.main()


    




import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import dotenv
import pandas as pd

class SpotifyApi:
    def __init__(self):
        dotenv.load_dotenv(override=True)
        client_id = os.environ["CLIENT_ID"]
        client_secret = os.environ["CLIENT_SECRET"]
        credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=credentials_manager)

    def recherche_piste(self, titre: str, artiste: str) -> str:
        query = f"{titre} {artiste}"
        results = self.sp.search(query, type='track', limit=1)
        if results['tracks']['items']:
            return results['tracks']['items'][0]['uri']
        else:
            return ""

    def obtenir_audio(self, uri: str) -> str:
        try:
            track_id = uri.split(":")[-1]
            track = self.sp.track(track_id)
            return track['preview_url']
        except spotipy.SpotifyException as e:
            print(f"Erreur Spotify lors de l'obtention de l'audio : {e}")
            return ""
        except Exception as e:
            print(f"Erreur inattendue lors de l'obtention de l'audio : {e}")
            return ""

    def renvoyer_piste_audio(self, titre: str, artiste: str) -> str:
        uri = self.recherche_piste(titre, artiste)
        if uri:
            url = self.obtenir_audio(uri)
            print(f"URL de l'extrait audio : {url}")
            return url
        else:
            print(f"Piste non trouvée pour {titre} de {artiste}")
            return ""

    def ajouter_audio_dataframe(self, data_musique: pd.DataFrame) -> pd.DataFrame:
        data_musique['Audio'] = None
        for index, row in data_musique.iterrows():
            titre = row['Titre']
            artiste = row['Artiste']
            print(f"Processing {titre} by {artiste}")
            audio_url = self.renvoyer_piste_audio(titre, artiste)
            print(f"Audio URL: {audio_url}")
            data_musique.loc[index, 'Audio'] = audio_url
        return data_musique


if __name__ == "__main__":
    spotify_fetcher = SpotifyApi()
    data_musique = pd.DataFrame({'Date': [], 'Artiste': [], 'Titre': []})  
    table_carte = spotify_fetcher.ajouter_audio_dataframe(data_musique)
    table_carte.to_csv("table_carte.csv", sep=";")
