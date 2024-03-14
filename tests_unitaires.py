import unittest
from unittest.mock import MagicMock, patch
from apy.py import SpotifyAPI  

class TestSpotifyAPI(unittest.TestCase):
    def setUp(self):
        self.spotify_api = SpotifyAPI()

    @patch('spotipy.Spotify.search')
    def test_recherche_piste(self, mock_search):
        # Mock de la réponse de l'API Spotify
        mock_search.return_value = {'tracks': {'items': [{'uri': 'mocked_uri'}]}}

        # Test de la méthode recherche_piste
        uri = self.spotify_api.recherche_piste('MockedTitle', 'MockedArtist')
        self.assertEqual(uri, 'mocked_uri')

    @patch('spotipy.Spotify.track')
    def test_obtenir_audio(self, mock_track):
        # Mock de la réponse de l'API Spotify
        mock_track.return_value = {'preview_url': 'mocked_url'}

        # Test de la méthode obtenir_audio
        url = self.spotify_api.obtenir_audio('mocked_uri')
        self.assertEqual(url, 'mocked_url')

    @patch('spotify_api_module.SpotifyAPI.recherche_piste')
    @patch('spotify_api_module.SpotifyAPI.obtenir_audio')
    def test_renvoyer_piste_audio(self, mock_obtenir_audio, mock_recherche_piste):
        # Mock des méthodes internes
        mock_recherche_piste.return_value = 'mocked_uri'
        mock_obtenir_audio.return_value = 'mocked_url'

        # Test de la méthode renvoyer_piste_audio
        url = self.spotify_api.renvoyer_piste_audio('MockedTitle', 'MockedArtist')
        self.assertEqual(url, 'mocked_url')

    @patch('spotify_api_module.SpotifyAPI.recherche_piste')
    def test_renvoyer_piste_audio_not_found(self, mock_recherche_piste):
        # Mock de la méthode recherche_piste pour simuler un résultat non trouvé
        mock_recherche_piste.return_value = None

        # Test de la méthode renvoyer_piste_audio pour le cas où la piste n'est pas trouvée
        url = self.spotify_api.renvoyer_piste_audio('NonExistentTitle', 'NonExistentArtist')
        self.assertIsNone(url)

if __name__ == '__main__':
    unittest.main()





import unittest
from unittest.mock import MagicMock, patch
from code_propre.py import WikipediaScraper  

class TestWikipediaScraper(unittest.TestCase):
    def setUp(self):
        self.url = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"
        self.target_date = "4/11/1984"
        self.scraper = WikipediaScraper(self.url)

    @patch('wikipedia_scraper_module.WikipediaScraper.create_dataframe')
    def test_scrape_data(self, mock_create_dataframe):
        # Mock de la méthode create_dataframe
        mock_create_dataframe.return_value = MagicMock()

        # Test de la méthode scrape_data
        self.scraper.scrape_data(self.target_date)
        self.assertTrue(self.scraper.scraping_started)
        mock_create_dataframe.assert_called_once()

    @patch('pandas.DataFrame.to_csv')
    @patch('wikipedia_scraper_module.WikipediaScraper.create_dataframe')
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
    @patch('wikipedia_scraper_module.WikipediaScraper.create_dataframe')
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
    


# class WikipediaScraper:
#     def __init__(self, url):
#         self.url = url
#         self.response = requests.get(self.url)
#         self.html = self.response.content
#         self.soup = BeautifulSoup(self.html, 'html.parser')
#         self.table_rows = self.soup.find_all('tr')
#         self.data = []
#         self.scraping_started = False

#     def scrape_data(self, target_date):
#         for row in self.table_rows:
#             if target_date in row.text:
#                 self.scraping_started = True
#             if self.scraping_started:
#                 cols = row.find_all('td')
#                 cols = [ele.text.strip() for ele in cols]
#                 self.data.append(cols)

#     def create_dataframe(self):
#         columns = ['N°', 'Date', 'Artiste', 'Titre', 'Nombre de semaines n°1', 'Commentaires']
#         data_musique = pd.DataFrame(self.data, columns=columns)
#         data_musique = data_musique.dropna()
#         data_musique = data_musique.reset_index(drop=True)
#         return data_musique

#     def save_to_csv(self, file_path, delimiter=';'):
#         data_frame = self.create_dataframe()
#         data_frame.to_csv(file_path, sep=delimiter)

# # Scrapping 
# url_de_la_page = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"
# target_date = "4/11/1984"
# scraper = WikipediaScraper(url_de_la_page)
# scraper.scrape_data(target_date)
# scraper.save_to_csv("/home/ensai/Bureau/Conception de logiciel/projet/projet_conception_logiciel/Musique.csv")