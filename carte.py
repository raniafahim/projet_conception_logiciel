import pandas as pd 
from api import renvoyer_piste_audio
from code_propre import data_musique

table_carte = data_musique[['Date', 'Artiste', 'Titre']]

table_carte.to_csv("/home/ensai/Documents/conception_logiciel/table_carte.csv",sep=";",index_label='id')



