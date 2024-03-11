from bs4 import BeautifulSoup
from requests import get
import pandas as pd
from datetime import datetime



result=[]
base = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"
page = get(base)
soup = BeautifulSoup(page.text, "html.parser")
liste_soup = soup.find_all("div", {"class": "mw-content-text-ltr mw-parser-output"})


annee = offre.append(annonce.find("span", {"class": "mw-headline"}).find_next_sibling("id").get_text(strip=True))

table_musique=find_all("table",{"class"="wikitable sortable jquery-tablesorter"})
ligne_musique= offre.append(annonce.find("th", {"class": "headsort"}).find_next_sibling("tr")
                            numero_musique=find_all("tr").get_text())

result = []
for i in range(1,2) :
    base = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"
    page = get(base)
    soup = BeautifulSoup(page.text, "html.parser")
    liste_soup = soup.find_all("div", {"class": "mw-content-text-ltr mw-parser-output"})



    for ol in liste_soup:
            annonces = ol.find_all("li", {"class": "results__item"})

            for annonce in annonces:
                        offre = []

                        # # Titre de l'annonce
                        #
                        # try:
                        #     offre.append(annonce.find("h2", {"class" : "job__title"}).a.attrs['title'])
                        # except :
                        #     offre.append("NA")




                        # Titre de l'annonce
                        #titre = annonce.find("h2", {"class": "job__title"})
                        annee = offre.append(annonce.find("span", {"class": "mw-headline"}).find_next_sibling("id").get_text(strip=True))
                        if not titre:  # Si le titre n'est pas dans un h2, cherchez dans un h3
                            titre = annonce.find("h3", {"class": "job__title"})

                        if titre and titre.a:  # Vérifiez que le titre et le lien a existent
                            offre.append(titre.a.get('title', "NA"))  # Utilisez .get pour éviter KeyError si 'title' n'existe pas
                        else:
                            offre.append("NA")



                        # # Lien de l'annonce
                        # try :
                        #     offre.append(base+annonce.find("h2",{"class" : "job__title"}).a.attrs['href'])
                        # except :
                        #     offre.append("NA")




                        # Lien de l'annonce
                        lien = annonce.find("h2", {"class": "job__title"})
                        if not lien:  # Si le lien n'est pas dans un h2, cherchez dans un h3
                            lien = annonce.find("h3", {"class": "job__title"})

                        if lien and lien.a:  # Vérifiez que le lien a existe
                            offre.append(base + lien.a.get('href', "").strip())
                        else:
                            offre.append("NA")



                        #
                        #
                        # # Date de l'annonce
                        # try :
                        #     offre.append(annonce.find("p", {"class":"job__posted-by"})['datetime'])
                        # except :
                        #     offre.append("NA")
                        #
                        #
                        #


                        # Localisation de l'emploi

                        try :
                            offre.append(annonce.find("dd", {"class":"job__details-value location"}).find("span").text.strip())
                        except :
                            offre.append("NA")





                        # Type de contrat de l'emploi

                        try :
                            offre.append(annonce.find("dt", {"class": "job__details-term job-type"}).find_next_sibling("dd").get_text(strip=True))
                        except :
                            offre.append("NA")


                        # Salary


                        try:
                            texte_salaire = annonce.find("dd", {"class":"job__details-value salary"}).get_text(strip=True)
                            texte_salaire = ' '.join(texte_salaire.split())  # Nettoie les espaces superflus
                            offre.append(texte_salaire)

                            # Extraction des plages salariales ou montants individuels
                            if "-" in texte_salaire:  # Gère les plages salariales
                                borne_inf, borne_sup = texte_salaire.split('-')[:2]
                                borne_inf = borne_inf.split('/')[0].strip()  # Sépare le montant du salaire des mots supplémentaires
                                borne_sup = borne_sup.split('/')[0].strip()
                                offre.append(borne_inf)
                                offre.append(borne_sup)
                            else:
                                salaire_unique = texte_salaire.split('/')[0].strip()  # Sépare le montant du salaire des mots supplémentaires
                                offre.append(salaire_unique)  # Ajoute le salaire unique à la fois comme salaire minimum et maximum
                                offre.append(salaire_unique)  # Salaires min et max sont égaux

                        except AttributeError:  # Si l'élément n'est pas trouvé ou s'il manque des données
                            offre.extend(["NA", "NA", "NA"])  # Ajoute trois "NA" pour le salaire, borne_inf et borne_sup


                        # Type salaire

                        try:

                            texte_salaire = annonce.find("dd", {"class":"job__details-value salary"}).get_text(strip=True)
                            texte_salaire = ' '.join(texte_salaire.split())  # Nettoie les espaces superflus

                            # Extraction du type de contrat après le "/"
                            type_contrat = "NA"
                            if "/" in texte_salaire:
                                type_contrat = texte_salaire.split('/')[1].strip()
                                offre.append(type_contrat)  # Ajoute le type de contrat extrait


                        except:
                            offre.append("NA")




                        # Descriptif de l'emploi

                        try :
                            offre.append(annonce.find("p", {"class":"job__description noscript-show"}).get_text(strip=True))
                        except :
                            offre.append("NA")
                        result.append(offre)



#
# data_salaries = pd.DataFrame(result, columns=[
#     "Emploi",
#     "Lien internet",
#     "Localisation",
#     "Statut",
#     "Salaire",
#     "Salaire minimum",  # Add this column if you have minimum salary data
#     "Salaire maximum", # Add this column if you have maximum salary data
#     "Descriptif"
# ])




data_salaries = pd.DataFrame(result, columns = ["Emploi", "URL", "Localisation", "Statut", "Salaire", "Salaire minimum", "Salaire maximum","Type de salaire", "Descriptif"])


data_salaries.to_csv("/home/ensai/Bureau/Conception de logiciel/projet/projet_conception_logiciel/Emploi3.csv",sep=";",encoding='utf-8-sig',index_label='id')

# data_salaries = pd.DataFrame(result, columns = ["Emploi", "Lien internet", "Date", "Localisation", "Statut", "Salaire", "Descriptif"])



# data_salaries['pays'] = 'FRANCE'




# https://www.cv-library.co.uk/jobs?us=1

# Heure = 13h35
# Heure = 13h40
# Heure = 13h51 echec








result = []
for i in range(1,2) :
    base = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France"
    lien = "https://fr.wikipedia.org/wiki/Liste_des_singles_num%C3%A9ro_un_en_France/page="
    page = get(lien+str(i))
    soup = BeautifulSoup(page.text, "html.parser")
    liste_soup = soup.find_all("ol", {"h3": "span"})



    for ol in liste_soup:
            annonces = ol.find_all("table", {"class": "wikitable sortable j query-tablesorter"})

            for annonce in annonces:
                        offre = []

                        # # Titre de l'annonce
                        #
                        # try:
                        #     offre.append(annonce.find("h2", {"class" : "job__title"}).a.attrs['title'])
                        # except :
                        #     offre.append("NA")




                        # Titre de la chanson
                        titre = annonce.find("a", {"href": "title"})
                        if not titre:  # Si le titre n'est pas dans un h2, cherchez dans un h3
                            titre = annonce.find("h3", {"class": "job__title"})

                        if titre and titre.a:  # Vérifiez que le titre et le lien a existent
                            offre.append(titre.a.get('title', "NA"))  # Utilisez .get pour éviter KeyError si 'title' n'existe pas
                        else:
                            offre.append("NA")



                        # # Lien de l'annonce
                        # try :
                        #     offre.append(base+annonce.find("h2",{"class" : "job__title"}).a.attrs['href'])
                        # except :
                        #     offre.append("NA")




                        # Lien de l'annonce
                        lien = annonce.find("h2", {"class": "job__title"})
                        if not lien:  # Si le lien n'est pas dans un h2, cherchez dans un h3
                            lien = annonce.find("h3", {"class": "job__title"})

                        if lien and lien.a:  # Vérifiez que le lien a existe
                            offre.append(base + lien.a.get('href', "").strip())
                        else:
                            offre.append("NA")



                        #
                        #
                        # # Date de l'annonce
                        # try :
                        #     offre.append(annonce.find("p", {"class":"job__posted-by"})['datetime'])
                        # except :
                        #     offre.append("NA")
                        #
                        #
                        #


                        # Localisation de l'emploi

                        try :
                            offre.append(annonce.find("dd", {"class":"job__details-value location"}).find("span").text.strip())
                        except :
                            offre.append("NA")





                        # Type de contrat de l'emploi

                        try :
                            offre.append(annonce.find("dt", {"class": "job__details-term job-type"}).find_next_sibling("dd").get_text(strip=True))
                        except :
                            offre.append("NA")


                        # Salary




                        try:
                            texte_salaire = annonce.find("dd", {"class":"job__details-value salary"}).get_text(strip=True)
                            texte_salaire = ' '.join(texte_salaire.split())  # Nettoie les espaces superflus
                            offre.append(texte_salaire)

                            # Extraction des plages salariales ou montants individuels
                            if "-" in texte_salaire:  # Gère les plages salariales
                                borne_inf, borne_sup = texte_salaire.split('-')[:2]
                                borne_inf = borne_inf.split('/')[0].strip()  # Sépare le montant du salaire des mots supplémentaires
                                borne_sup = borne_sup.split('/')[0].strip()
                                offre.append(borne_inf)
                                offre.append(borne_sup)
                            else:
                                salaire_unique = texte_salaire.split('/')[0].strip()  # Sépare le montant du salaire des mots supplémentaires
                                offre.append(salaire_unique)  # Ajoute le salaire unique à la fois comme salaire minimum et maximum
                                offre.append(salaire_unique)  # Salaires min et max sont égaux

                        except AttributeError:  # Si l'élément n'est pas trouvé ou s'il manque des données
                            offre.extend(["NA", "NA", "NA"])  # Ajoute trois "NA" pour le salaire, borne_inf et borne_sup
                        #
                        # try:
                        #     texte_salaire = annonce.find("dd", {"class":"job__details-value salary"}).get_text(strip=True)
                        #     texte_salaire = ' '.join(texte_salaire.split())  # Nettoie les espaces superflus
                        #
                        #     # Extraction du type de contrat après le "/"
                        #     type_contrat = "NA"
                        #     if "/" in texte_salaire:
                        #         type_contrat = texte_salaire.split('/')[1].strip()
                        #
                        #
                        #     offre.append(type_contrat)  # Ajoute le type de contrat extrait
                        #     offre.append(texte_salaire)  # Ajoute le texte complet du salaire
                        #
                        #     # Extraction des plages salariales ou montants individuels
                        #     if "-" in texte_salaire:  # Gère les plages salariales
                        #         borne_inf, borne_sup = texte_salaire.split('-')[:2]
                        #         borne_inf = borne_inf.split('/')[0].strip()  # Sépare le montant du salaire des mots supplémentaires
                        #         borne_sup = borne_sup.split('/')[0].strip()
                        #         offre.append(borne_inf)  # Ajoute le salaire minimum
                        #         offre.append(borne_sup)  # Ajoute le salaire maximum
                        #     else:
                        #         salaire_unique = texte_salaire.split('/')[0].strip()  # Sépare le montant du salaire des mots supplémentaires
                        #         offre.append(salaire_unique)  # Ajoute le salaire unique à la fois comme salaire minimum et maximum
                        #         offre.append(salaire_unique)
                        #
                        #     # offre.append(type_contrat)  # Ajoute le type de contrat extrait
                        #
                        # except AttributeError:  # Si l'élément n'est pas trouvé ou s'il manque des données
                        #     offre.extend(["NA", "NA", "NA", "NA","NA"])  # Ajoute cinq "NA" pour le salaire, borne_inf, borne_sup, type de contrat
                        #


                        # Descriptif de l'emploi

                        try :
                            offre.append(annonce.find("p", {"class":"job__description noscript-show"}).get_text(strip=True))
                        except :
                            offre.append("NA")
                        result.append(offre)



#
# data_salaries = pd.DataFrame(result, columns=[
#     "Emploi",
#     "Lien internet",
#     "Localisation",
#     "Statut",
#     "Salaire",
#     "Salaire minimum",  # Add this column if you have minimum salary data
#     "Salaire maximum", # Add this column if you have maximum salary data
#     "Descriptif"
# ])

data_salaries = pd.DataFrame(result, columns=[
    "Emploi",
    "Lien internet",
    "Localisation",
    "Statut",
    "Salaire",
    "Type de salaire",
    "Salaire minimum",
    "Salaire maximum",
    "Type contrat",  # Nouvelle colonne pour le type de contrat
    "Descriptif"
])


# data_salaries = pd.DataFrame(result, columns = ["Emploi", "Lien internet", "Date", "Localisation", "Statut", "Salaire", "Descriptif"])


# "Type de salaire", "Salaire minimum", "Salaire maximum"

data_salaries.to_csv("/home/ensai/Bureau/Conception de logiciel/projet/projet_conception_logiciel/Emploi2.csv",sep=";",encoding='utf-8-sig')



# data_salaries['pays'] = 'FRANCE'

