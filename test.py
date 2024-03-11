import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv 



# Remplacez 'url_de_la_page' par l'URL réelle de la page que vous souhaitez scraper.
url_de_la_page = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"

response = requests.get(url_de_la_page)
html = response.content

soup = BeautifulSoup(html, 'html.parser')
table_rows = soup.find_all('tr')

data = []
for row in table_rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)  # Get rid of empty values

for row in data: 
    print(row)











#print(data)

#print(type(data))




data_salaries = pd.DataFrame(data, columns = ["Emploi", "URL", "Localisation", "Statut", "Descriptif","ffdf"])

print(data_salaries)


data_salaries.to_csv("/home/ensai/Bureau/Conception de logiciel/projet/projet_conception_logiciel/Emploi4.csv",sep=";",index_label='id')


# print(type(data))