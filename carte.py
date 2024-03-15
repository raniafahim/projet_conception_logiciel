import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import qrcode
#from api import data_musique
from datetime import datetime

"06/01/1985;Peter et Sloane;Besoin de rien, envie de toi"
data = {
    'Artiste': ['Artiste1', 'Artiste2', 'Artiste3','Peter et Sloane','Artiste4'],
    'Titre': ['Titre1', 'Titre2', 'Titre3',"Besoin de rien, envie de toi"'Titre4',],
    'Date': ["04/11/1984", "4/11/1984", "04/11/1984","04/11/1984","06/01/1985"],
    'Audio': ['http://lien-audio-1', 'http://lien-audio-2', 'http://lien-audio-3', "https://p.scdn.co/mp3-preview/391b635047403beaec61ac63d502ae64ebd84f31?cid=4d3bffd173c84f21ab47981ba6cd15f8",'http://lien-audio-4']
}


ma_table_test = pd.DataFrame(data)


def generer_carte(pdf, artiste, titre, date, audio_url):
    # Convertir la date en objet datetime
    date_obj = datetime.strptime(date, "%d/%m/%Y")
    
    # Dessiner la bordure de la carte
    pdf.setStrokeColorRGB(0.5, 0, 0.5)  # Violet
    pdf.rect(10, 10, 280, 380)
    
    # Dessiner le recto de la carte avec le QR code
    pdf.setFillColorRGB(0.5, 0, 0.5)  # Violet
    pdf.rect(15, 15, 270, 170, fill=True)
    
    # Ajouter le QR code au recto de la carte
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=6,
        border=1,
    )
    qr.add_data(audio_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    pdf.drawInlineImage(img, 70, 20, width=150, height=160)
    
    # Dessiner le verso de la carte
    pdf.showPage()
    pdf.setFillColorRGB(0, 0, 0)
    
    # Ajouter le titre de l'artiste au verso
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawCentredString(150, 350, artiste)
    
    # Ajouter la date de la chanson au verso
    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(150, 320, date_obj.strftime("%d/%m/%Y"))
    
    # Ajouter le titre de la chanson au verso
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawCentredString(150, 240, titre)

def generer_pdf(data_frame):
    pdf_path = "playlist_test.pdf"
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
