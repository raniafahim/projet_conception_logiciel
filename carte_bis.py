

import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import qrcode
#from api import data_musique
from datetime import datetime

from textwrap import wrap


data = {
    'Artiste': ['Artiste1', 'Artiste2', 'Artiste3','Peter et SloanePeter et SloanePeter et SloanePeter et SloanePeter et SloanePeter et Sloane ','Artiste4'],
    'Titre': ['Titre1', 'Titre2', 'Titre3',"Besoin de rien, envie de toi",'Titre4',],
    'Date': ["04/11/1984", "4/11/1984", "04/11/1984","04/11/1984","06/01/1985"],
    'Audio': ['http://lien-audio-1', 'http://lien-audio-2', 'http://lien-au"Besoin de rien, envie de toi"dio-3', "https://p.scdn.co/mp3-preview/391b635047403beaec61ac63d502ae64ebd84f31?cid=4d3bffd173c84f21ab47981ba6cd15f8",'http://lien-audio-4']
}


ma_table_test = pd.DataFrame(data)



def generer_carte(pdf, artiste, titre, date, audio_url):
    # Convertir la date en objet datetime
    date_obj = datetime.strptime(date, "%d/%m/%Y")
    
    # Définir les couleurs
    couleur_bordure = (0.5, 0, 0.5)  # Violet
    couleur_texte = (0, 0, 0)  # Noir
    
    # Taille de la carte
    largeur_carte = 300
    hauteur_carte = 200
    
    # Dessiner la bordure de la carte
    pdf.setStrokeColorRGB(*couleur_bordure)
    pdf.rect(10, 10, largeur_carte, hauteur_carte)
    
    # Dessiner le recto de la carte avec le QR code
    pdf.rect(15, 15, 270, 170)
    
    # Ajouter le QR code au recto de la carte
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=6,
        border=1,
    )
    qr.add_data(audio_url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    pdf.drawInlineImage(qr_img, 70, 20, width=150, height=150)
    
    # Dessiner le verso de la carte
    pdf.showPage()
    
    # Dessiner la bordure du verso de la carte
    pdf.setStrokeColorRGB(*couleur_bordure)
    pdf.rect(10, 10, largeur_carte, hauteur_carte)
    
    # Ajouter le titre de l'artiste au verso
    pdf.setFillColorRGB(*couleur_texte)
    pdf.setFont("Helvetica-Bold", 18)
    artiste_lines = wrap(artiste, width=30)  # Ajuster pour tenir dans la carte
    artiste_start_y = 160
    for line in artiste_lines:
        pdf.drawCentredString(largeur_carte / 2, artiste_start_y, line)
        artiste_start_y -= 15
    
    # Ajouter la date de la chanson au verso
    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(largeur_carte / 2, 150, date_obj.strftime("%d/%m/%Y"))
    
    # Ajouter le titre de la chanson au verso
    pdf.setFont("Helvetica-Bold", 14)
    titre_lines = wrap(titre, width=30)  # Ajuster pour tenir dans la carte
    titre_start_y = 110
    for line in titre_lines:
        pdf.drawCentredString(largeur_carte / 2, titre_start_y, line)
        titre_start_y -= 15


def generer_pdf(data_frame):
    pdf_path = "playlist_test_bis.pdf"
    pdf = canvas.Canvas(pdf_path, pagesize=letter)

    for index, row in data_frame.iterrows():
        artiste = row['Artiste']
        titre = row['Titre']
        date = row['Date']
        audio_url = row['Audio']

        generer_carte(pdf, artiste, titre, date, audio_url)

    pdf.save()


if __name__ == "__main__":
    generer_pdf(ma_table_test)