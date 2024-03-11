import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv 



url_de_la_page = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"

response = requests.get(url_de_la_page)
html = response.content

soup = BeautifulSoup(html, 'html.parser')
table_rows = soup.find_all('tr')

data = []
scraping_started = False  

for row in table_rows:
    if "4/11/1984" in row.text:
        scraping_started = True  
    if scraping_started:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols) 


# for row in data: 
#     print(row)



data_musique = pd.DataFrame(data, columns = ['N°', 'Date', 'Artiste', 'Titre', 'Nombre de semaines n°1', 'Commentaires'])



data_musique= data_musique.dropna()
data_musique = data_musique.reset_index(drop=True)



data_musique.to_csv("/home/ensai/Bureau/Conception de logiciel/projet/projet_conception_logiciel/Musique2.csv",sep=";")
