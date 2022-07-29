#Importation de modules
import mysql.connector
import csv 
from urllib.parse import urlparse 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Déclaration des variables
resultat = ""
# recherche = []
categorie_resultat = ""

#Connexion au base de données
db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "root",
  database = "domaines"
)

#Demande du fichier à l'utilisateur
csv_file = input("insérer chemin d'accès du csv :")

#Ouverture de l'historique CSV  
historique = open(csv_file,'r')

#Ouverture du CSV de résultat 
header = ['categorie', 'nbfois']

CSV_result = open('resultat_csv.csv', 'w', newline='')

writer = csv.writer(CSV_result, delimiter=';')

# Écriture de entête
writer.writerow(header)

#Création du tableau des résultats 
value = []

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
    print(r.text)
    global resultat_bluecoat
    resultat_bluecoat = r.text
    
    print(resultat_bluecoat)
  # Fermeture de la fenêtre
  driver.close()

lecture = csv.DictReader(historique)
for ligne in lecture :
  historique_url = ligne['URL']
  
  #Fonction de recherche du nom de domaine 
  result_url = urlparse(historique_url)
  resultat = result_url.hostname
  print(resultat)

  #Fonction de recherche du nom de domaine 
  # recherche = [pos for pos, char in enumerate(historique_url) if char == "/"] 
  # for i in range(recherche[1],recherche[2]) :
  #     resultat = resultat + historique_url[i]
  
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
  sql_result = resultat_sql[0]
  data_sql = [sql_result, 1]
  writer.writerow(data_sql)
  
  #Reinitialisation des variables 
  requete_domaine = ""
  result_url = ""
  
  if res == False :
    demande_bluecoat(resultat)
    
    # Écriture des données 
    data_bluecoat = [resultat_bluecoat, 1]
    writer.writerow(data_bluecoat)
    
    value.append([resultat,resultat_bluecoat])
    
    resultat = ""

print(value)

#Créer un curseur de base de données pour effectuer des opérations SQL
cur = db.cursor()
insertion_requete = "INSERT INTO `domaines`(`domaine`, `categorie`) VALUES (%s,%s)"

cur.executemany(insertion_requete,value)
db.commit()
print(cur.rowcount, "nouveaux domaines et catégories ont été insérés.")

db.close()
historique.close()
CSV_result.close()
