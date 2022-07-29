#Importation de module
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Déclaration des variables
url = input("saisissez l'url : ")
resultat = ""
recherche = []
test = ""
demande = "https://sitereview.bluecoat.com/#/lookup-result"#Site de BlueCoat

#Fonction de recherche du nom de domaine
recherche = [pos for pos, char in enumerate(url) if char == "/"]
for i in range(recherche[1],recherche[2]):
    resultat = resultat + url[i]
resultat = resultat[1:]
print(resultat)

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

#Fermeture de la fenêtre
driver.close()

print(test)
