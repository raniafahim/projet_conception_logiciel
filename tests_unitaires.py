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
from api import SpotifyApi # Assurez-vous de remplacer 'votre_module' par le nom de votre fichier

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


    

