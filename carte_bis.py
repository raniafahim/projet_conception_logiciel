import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
import qrcode
from datetime import datetime

data = {
    'Artiste': ['Artiste1', 'Artiste2', 'Artiste3', 'Peter et Sloane', 'Artiste4'],
    'Titre': ['Titre1', 'Titre2', 'Titre3', "Besoin de rien, envie de toi", 'Titre4'],
    'Date': ["04/11/1984", "4/11/1984", "04/11/1984", "04/11/1984", "06/01/1985"],
    'Audio': [
        'http://lien-audio-1', 'http://lien-audio-2', 'http://lien-audio-3',
        "https://p.scdn.co/mp3-preview/391b635047403beaec61ac63d502ae64ebd84f31?cid=4d3bffd173c84f21ab47981ba6cd15f8",
        'http://lien-audio-4'
    ]
}
ma_table_test = pd.DataFrame(data)

def generer_carte(pdf, artiste, titre, date, audio_url, verso=False):
    date_obj = datetime.strptime(date, "%d/%m/%Y")
    
    if verso:
        # Paramètres du verso de la carte
        pdf.setFillColorRGB(0.8, 0.5, 0.5)  # Couleur de fond claire pour le verso
        pdf.rect(10, 10, 280, 180, fill=True, stroke=False)
        
        # Informations de l'artiste et titre
        pdf.setFillColorRGB(0, 0, 0)  # Noir pour le texte
        pdf.setFont("Helvetica-Bold", 24)
        pdf.drawString(15, 150, date.split('/')[2])  # Année
        
        pdf.setFont("Helvetica", 18)
        pdf.drawString(15, 120, titre)
        
        pdf.setFont("Helvetica", 12)
        pdf.drawString(15, 90, artiste)
    
    else:
        # Paramètres du recto de la carte avec le QR code
        pdf.setFillColorRGB(0.8, 0.1, 0.2)  # Blanc pour le fond du recto
        pdf.rect(10, 10, 280, 180, fill=True, stroke=False)
        
        # QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=1,
        )
        qr.add_data(audio_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Position du QR code au centre
        qr_size = 80 * mm
        qr_x = (280 - qr_size) / 2
        qr_y = (180 - qr_size) / 2 + 20
        pdf.drawInlineImage(img, qr_x, qr_y, width=qr_size, height=qr_size)

def generer_pdf(data_frame):
    pdf_path = "playlist_amelioree3.pdf"
    pdf = canvas.Canvas(pdf_path, pagesize=landscape(letter))

    for index, row in data_frame.iterrows():
        generer_carte(pdf, row['Artiste'], row['Titre'], row['Date'], row['Audio'], verso=False)
        pdf.showPage()  # Créer une nouvelle page pour le verso
        generer_carte(pdf, row['Artiste'], row['Titre'], row['Date'], row['Audio'], verso=True)
        pdf.showPage()  # Préparer la page suivante pour une nouvelle carte

    pdf.save()

if __name__ == "__main__":
    generer_pdf(ma_table_test)


