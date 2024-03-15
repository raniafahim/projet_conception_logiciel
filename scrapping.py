import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv 



import requests
from bs4 import BeautifulSoup
import pandas as pd

class WikipediaScraper:
    """
    Scrapper pour extraire des données de tableaux à partir d'une page Wikipedia.

    Attributes:
        url (str): URL de la page Wikipedia à scraper.
        response (requests.Response): Réponse HTTP obtenue après requête GET de l'URL.
        soup (BeautifulSoup): Objet BeautifulSoup pour parse le contenu HTML de la page.
        table_rows (ResultSet): Ensemble des lignes de tableau (<tr>) trouvées dans la page.
        data (list): Liste pour stocker les données extraites des tableaux.
        scraping_started (bool): Indicateur pour commencer l'extraction à partir d'une date cible.
    """
    def __init__(self, url):
        """
        Initialise le scraper avec l'URL donnée et prépare le contenu pour le scraping.

        Parameters:
            url (str): L'URL de la page Wikipedia à scraper.
        """
        self.url = url
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.table_rows = self.soup.find_all('tr')
        self.data = []
        self.scraping_started = False

    def scrape_data(self, target_date):
        """
        Extrait les données du tableau à partir de la date cible.

        Parameters:
            target_date (str): La date à partir de laquelle l'extraction des données commence.
        """
        for row in self.table_rows:
            if target_date in row.text:
                self.scraping_started = True
            if self.scraping_started:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                self.data.append(cols)

    def create_dataframe(self):
        """
        Crée un DataFrame à partir des données extraites.

        Returns:
            pandas.DataFrame: DataFrame contenant les données extraites et nettoyées.
        """
        columns = ['N°', 'Date', 'Artiste', 'Titre', 'Nombre de semaines n°1', 'Commentaires']
        data_musique = pd.DataFrame(self.data, columns=columns)
        data_musique = data_musique.dropna()
        data_musique = data_musique.reset_index(drop=True)
        return data_musique

    def save_to_csv(self, file_name, delimiter=';'):
        """
        Sauvegarde le DataFrame dans un fichier CSV.

        Parameters:
            file_name (str): Le nom du fichier où sauvegarder les données.
            delimiter (str): Le délimiteur à utiliser pour le fichier CSV, ';' par défaut.
        """
        data_frame = self.create_dataframe()
        data_frame.to_csv(file_name, sep=delimiter)




# Scrapping 
url_de_la_page = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"
target_date = "4/11/1984"
scraper = WikipediaScraper(url_de_la_page)
scraper.scrape_data(target_date)
data_musique = scraper.create_dataframe()
scraper.save_to_csv("Musique.csv")





