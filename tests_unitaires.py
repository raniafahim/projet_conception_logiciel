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
from unittest.mock import MagicMock, patch
from scrapping import WikipediaScraper  

class TestWikipediaScraper(unittest.TestCase):
    def setUp(self):
        self.url = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"
        self.target_date = "4/11/1984"
        self.scraper = WikipediaScraper(self.url)

    @patch('scrapping.WikipediaScraper.create_dataframe')
    def test_scrape_data(self, mock_create_dataframe):
        # Mock de la méthode create_dataframe
        mock_create_dataframe.return_value = MagicMock()

        # Test de la méthode scrape_data
        self.scraper.scrape_data(self.target_date)
        self.assertTrue(self.scraper.scraping_started)
        mock_create_dataframe.assert_called_once()

    @patch('pandas.DataFrame.to_csv')
    @patch('scrapping.WikipediaScraper.create_dataframe')
    def test_save_to_csv(self, mock_create_dataframe, mock_to_csv):
        # Mock de la méthode create_dataframe et de la méthode to_csv
        mock_create_dataframe.return_value = MagicMock()
        mock_to_csv.return_value = None

        # Test de la méthode save_to_csv
        file_path = "/home/ensai/Bureau/Conception de logiciel/projet/projet_conception_logiciel/Musique.csv"
        self.scraper.save_to_csv(file_path)
        mock_create_dataframe.assert_called_once()
        mock_to_csv.assert_called_once_with(file_path, sep=';')

    @patch('requests.get')
    @patch('scrapping.WikipediaScraper.create_dataframe')
    def test_init(self, mock_create_dataframe, mock_requests_get):
        # Mock de la méthode create_dataframe et de la méthode requests.get
        mock_create_dataframe.return_value = MagicMock()
        mock_requests_get.return_value = MagicMock()

        # Test de la méthode init
        scraper = WikipediaScraper(self.url)
        self.assertIsNotNone(scraper.response)
        mock_create_dataframe.assert_called_once()
        mock_requests_get.assert_called_once_with(self.url)

if __name__ == '__main__':
    unittest.main()




    

