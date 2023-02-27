# Symantec-Sitereview 

Ceci est un script python permettant grâce à un export d'historique de navigation de savoir à quelle catégorie appartient le site avec l'aide d'une base de données locale provenant de l'université de Toulouse et du site Symantec Sitereview.

## Installation

Assurez-vous d'avoir Python 3 installé sur votre ordinateur.

Il se compose de plusieurs librairies python : MySQL connector, CSV, Selenium, URLLIB et time. seule selenium et mysql-connector demande une installation grâce à Pip.

`
pip install selenium
`

`
pip install mysql-connector
`

Clonez ce projet ou téléchargez-le en tant que fichier ZIP.

Ouvrez un terminal et accédez au répertoire contenant le script.

Il sera nécessaire un serveur MySQL pour importer la base de données (j'utilise MAMP pour mon cas)

## Utilisation

Exécutez le script en utilisant la commande `python main.py`.

N'oubliez pas de changer le chemin d'accès du dirver chrome (ligne `66 driver = webdriver.Chrome(executable_path="chromedriver.exe"`)

## Ressources 

Fichier pour la base de donnée : https://dsi.ut-capitole.fr/blacklists/

Driver Chrome pour Selenium : https://sites.google.com/chromium.org/driver/

Symantec Sitereview : https://sitereview.bluecoat.com/#/
