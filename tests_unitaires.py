import unittest
from unittest.mock import MagicMock, patch
from scrapping import WikipediaScraper  
import os

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


    

import unittest
from unittest.mock import patch, MagicMock
import api  

class TestSpotifyFunctions(unittest.TestCase):
    @patch('api.sp.search')
    def test_recherche_piste_trouvee(self, mock_search):
        mock_search.return_value = {
            'tracks': {
                'items': [
                    {'uri': 'spotify:track:123'}
                ]
            }
        }
        
        uri = api.recherche_piste("titre", "artiste")
        self.assertEqual(uri, 'spotify:track:123')

    @patch('api.sp.search')
    def test_recherche_piste_non_trouvee(self, mock_search):
        mock_search.return_value = {'tracks': {'items': []}}
        uri = api.recherche_piste("titre", "artiste")
        self.assertEqual(uri, "")

    @patch('api.sp.track')
    def test_obtenir_audio_succes(self, mock_track):
        mock_track.return_value = {'preview_url': 'http://preview.url'}
        url = api.obtenir_audio("spotify:track:123")
        self.assertEqual(url, 'http://preview.url')

    @patch('api.sp.track', side_effect=Exception("Erreur"))
    def test_obtenir_audio_erreur(self, mock_track):
        url = api.obtenir_audio("spotify:track:123")
        self.assertEqual(url, "")

    @patch('api.obtenir_audio')
    @patch('api.recherche_piste')
    def test_renvoyer_piste_audio(self, mock_recherche_piste, mock_obtenir_audio):
        mock_recherche_piste.return_value = "spotify:track:123"
        mock_obtenir_audio.return_value = "http://preview.url"
        url = api.renvoyer_piste_audio("titre", "artiste")
        self.assertEqual(url, "http://preview.url")
        mock_recherche_piste.assert_called_once_with("titre", "artiste")
        mock_obtenir_audio.assert_called_once_with("spotify:track:123")

if __name__ == '__main__':
    unittest.main()

