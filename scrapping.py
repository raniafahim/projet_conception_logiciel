import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv 



class WikipediaScraper:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url)
        self.html = self.response.content
        #self.soup = BeautifulSoup(self.html, 'html.parser')  
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.table_rows = self.soup.find_all('tr')
        self.data = []
        self.scraping_started = False

    def scrape_data(self, target_date):
        for row in self.table_rows:
            if target_date in row.text:
                self.scraping_started = True
            if self.scraping_started:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                self.data.append(cols)

    def create_dataframe(self):
        columns = ['N°', 'Date', 'Artiste', 'Titre', 'Nombre de semaines n°1', 'Commentaires']
        data_musique = pd.DataFrame(self.data, columns=columns)
        data_musique = data_musique.dropna()
        data_musique = data_musique.reset_index(drop=True)
        return data_musique

    def save_to_csv(self, file_name, delimiter=';'):
        data_frame = self.create_dataframe()
        data_frame.to_csv(file_name, sep=delimiter)

# Scrapping 
url_de_la_page = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"
target_date = "4/11/1984"
scraper = WikipediaScraper(url_de_la_page)
scraper.scrape_data(target_date)
data_musique = scraper.create_dataframe()
scraper.save_to_csv("Musique.csv")





