import api
import carte
from scrapping import data_musique 

table_carte = data_musique[['Date', 'Artiste', 'Titre']].copy()
table_carte['Audio'] = None


for index, row in table_carte.iterrows():
    titre = row['Titre']
    artiste = row['Artiste']
    print(f"Processing {titre} by {artiste}")
    audio_url = api.renvoyer_piste_audio(titre, artiste)
    print(f"Audio URL: {audio_url}")
    table_carte.loc[index, 'Audio'] = audio_url

table_carte = table_carte.dropna()
table_carte = table_carte.reset_index(drop=True)
table_carte.to_csv("table_carte.csv",sep=";")   



carte.generer_pdf(table_carte,"cartes_hitster.pdf")