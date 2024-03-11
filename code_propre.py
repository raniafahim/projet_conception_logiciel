import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv 



# # Remplacez 'url_de_la_page' par l'URL réelle de la page que vous souhaitez scraper.
# url_de_la_page = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"

# response = requests.get(url_de_la_page)
# html = response.content

# soup = BeautifulSoup(html, 'html.parser')
# table_rows = soup.find_all('tr')

# data = []

# for row in table_rows:
#     cols = row.find_all('td')
#     cols = [ele.text.strip() for ele in cols]
#     data.append(cols)  # Get rid of empty values

# for row in data: 
#     print(row)


# print(data)
#table_musique=find_all("table",{"class"="wikitable sortable jquery-tablesorter"})
#ligne_musique= offre.append(annonce.find("th", {"class": "headsort"}).find_next_sibling("tr")
                            #numero_musique=find_all("tr").get_text())





url_de_la_page = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"

response = requests.get(url_de_la_page)
html = response.content

soup = BeautifulSoup(html, 'html.parser')
table_rows = soup.find_all('tr')

data = []
scraping_started = False  # Variable pour indiquer le début du scraping des données utiles

for row in table_rows:
    # Vérifiez si la ligne contient des informations utiles
    if "4/11/1984" in row.text:
        scraping_started = True  # Marquez le début du scraping des données utiles
    if scraping_started:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols)  # Ajoutez les données utiles à la liste

# Maintenant, vous pouvez traiter vos données comme auparavant
for row in data: 
    print(row)



data_musique = pd.DataFrame(data, columns = ['N°', 'Date', 'Artiste', 'Titre', 'Nombre de semaines n°1', 'Commenraires'])



data_musique.to_csv("/home/ensai/Bureau/Conception de logiciel/projet/projet_conception_logiciel/Musique.csv",sep=";",index_label='id')


# url_de_la_page = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"

# response = requests.get(url_de_la_page)
# html = response.content

# soup = BeautifulSoup(html, 'html.parser')
# table_rows = soup.find_all('tr')

# data = []
# scraping_started = False

# for row in table_rows:
#     if "1" in row.text:
#         scraping_started = True
#     if scraping_started:
#         cols = row.find_all('td')
        
#         # Vérifiez que la liste cols a suffisamment d'éléments avant d'accéder à un élément spécifique
#         if len(cols) >= 2:
#             cols = [ele.text.strip() for ele in cols]
            
#             # Group the dates in the same column
#             date_range = cols[1].replace(',', ' ').split()
#             cols[1] = '-'.join(date_range)
            
#             data.append(cols)

# data_salaries = pd.DataFrame(data, columns=['ID', 'Dates', 'Artist', 'Title', 'Weeks', 'Notes'])

# data_salaries.to_csv("/home/ensai/Bureau/Conception de logiciel/projet/projet_conception_logiciel/Emploi2.csv", sep=";", index_label='id')

# print(data_salaries)