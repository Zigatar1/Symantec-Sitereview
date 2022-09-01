#Importation de modules
import mysql.connector
import csv
from urllib.parse import urlparse
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Déclaration des variables
resultat = ""
categorie_resultat = ""

#Connexion au base de données
db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "root",
  database = "domaines"
)

#Demande du fichier à l'utilisateur
csv_file = input("Insérer chemin d'accès du csv :")

#Ouverture de l'historique CSV
historique = open(csv_file,'r', encoding='UTF-8')

#Ouverture du CSV de résultat
CSV_result = open('resultat_csv.csv', 'w', newline='', encoding='UTF-8')

#Ecriture de l'entête
writer = csv.DictWriter(CSV_result, fieldnames=['URL', 'Catégorie', 'Date'])
writer.writeheader()

#Créer un curseur de base de données pour effectuer des opérations SQL
cur = db.cursor()

def demande_base_donnee(resultat):
  #Création de la requete SQL
  requete_domaine = "SELECT `categorie` FROM `domaines` WHERE `domaine`= '" + resultat + "'"
  print(requete_domaine)

  #Créer un curseur de base de données pour effectuer des opérations SQL
  cur = db.cursor()

  #Exécuter le curseur avec la méthode execute() et transmis la requête SQL
  cur.execute(requete_domaine)

  #Récupèrer toutes les lignes de la dernière instruction exécutée.
  global res
  res = cur.fetchall()

  #Affichage du résultat
  for line in res:
    print(line)
    global resultat_sql
    resultat_sql = line
    resultat_sql = resultat_sql[0]

  res = bool(res) 

def demande_bluecoat(resultat):
  #Site de BlueCoat
  demande = "https://sitereview.bluecoat.com/#/lookup-result"

  #Accès au site BlueCoat
  driver = webdriver.Chrome(executable_path="chromedriver.exe")
  driver.get(demande)

  #Barre de recherche "Saisissez une URL"
  champ_entrer = driver.find_element(By.ID, "txtUrl")#id de la barre de recherche
  champ_entrer.send_keys(resultat)

  #Bouton "Vérifier la catégorie"
  bouton = driver.find_element(By.ID, "btnLookup")#id du bouton de recherche
  bouton.click()

  #Délai pour la redirection
  time.sleep(1)

  #Récupérer la catégorie
  categorie = driver.find_elements(By.CLASS_NAME, "clickable-category")#id de la catégorie

  #Affichage de la catégorie
  print("L'url saissis appartient à la catégorie :")

  for r in categorie:
    global resultat_bluecoat
    resultat_bluecoat = r.text
    print(resultat_bluecoat)

  # Fermeture de la fenêtre
  driver.close()

lecture = csv.DictReader(historique)
for ligne in lecture :
  historique_url = ligne['URL']

  #Recherche dans l'entete du format Date/Heure 
  if 'Date/heure d’accès\xa0–\xa0UTC+01:00 (dd/MM/yyyy)[DST]' in ligne :
    date_url = ligne["Date/heure d’accès\xa0–\xa0UTC+01:00 (dd/MM/yyyy)[DST]"]#Edge
  else:
    date_url = ligne['Date/heure de la dernière visite\xa0–\xa0UTC+01:00 (dd/MM/yyyy)[DST]']#Chrome
  
  #Fonction de recherche du nom de domaine
  result_url = urlparse(historique_url)
  resultat = result_url.hostname
  print(resultat)

  if resultat != None :
    #Recherche du sous-domaine
    if "www." in resultat :
      resultat = resultat[4:]
    else:
      resultat = resultat[0:]
  else:
    resultat = "file"

  demande_base_donnee(resultat)

  # Écriture des données
  writer.writerow({'URL' : resultat, 'Catégorie': resultat_sql, 'Date': date_url})

  #Reinitialisation des variables
  requete_domaine = ""
  result_url = ""

  if res == False :
    demande_bluecoat(resultat)

    # Écriture des données
    writer.writerow({'URL' : resultat, 'Catégorie': resultat_bluecoat, 'Date': date_url})

    #Création d'un curseur de base de données pour effectuer des opérations SQL
    cur = db.cursor()

    #Création de la requête SQL pour l'ajout des catégories et domaines
    val = [resultat,resultat_bluecoat]
    insertion_requete = "INSERT INTO `domaines` (`domaine`, `categorie`) VALUES (%s, %s)" 
    cur.execute(insertion_requete,val)
    db.commit()

    print()
    resultat = ""

print(cur.rowcount, "nouveaux domaines et catégories ont été insérés.")

#Fermeture des différents fichiers
db.close()
historique.close()
CSV_result.close()