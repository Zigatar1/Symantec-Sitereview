# Python-HistoClassify 

Ceci est un script python permettant grâce à un export d'historique de navigation de savoir à quelle catégorie appartient le site avec l'aide d'une base de données locale provenant de l'université de Toulouse et du site Symantec Sitereview.

## Installation

Assurez-vous d'avoir Python 3 installé sur votre ordinateur.

Il se compose de plusieurs librairies python : MySQL connector, CSV, Selenium, URLLIB et time. Seule selenium et mysql-connector demande une installation grâce à Pip.

`
pip install selenium
`

`
pip install mysql-connector
`

Clonez ce projet ou téléchargez-le en tant que fichier ZIP.

Ouvrez un terminal et accédez au répertoire contenant le script.

Il sera nécessaire un serveur MySQL pour importer la base de données (j'utilise MAMP pour mon cas).

Pour l'initialisation de la base de données, il est nécessaire d'exécuter `BasedeDonnées_V2.py` en ayant reconstitué en un seul fichier `domains_adult.txt` et de modifier la ligne `3 mydb = mysql.connector.connect()` avec vos paramètres de connexion.

## Utilisation

Exécutez le script en utilisant la commande `python main.py`.

Lors de la demande du chemin d'accès, vous pouvez mettre un chemin complet ou raccourci s'il se trouve dans le même dossier.

N'oubliez pas de changer le chemin d'accès du driver chrome (ligne `66 driver = webdriver.Chrome(executable_path="chromedriver.exe"`).

`demande_base_donnee` intérroge la base de données local (ligne `14 db = mysql.connector.connect()` doit etre modifiée avec vos parametres de connexion à votre base de données).

`demande_bluecoat` intérroge la site bluecoat (https://sitereview.bluecoat.com/#/) si le nom de domaine n'est pas dans la base de données local.

## Ressources 

Fichier pour la base de donnée : https://dsi.ut-capitole.fr/blacklists/

Driver Chrome pour Selenium : https://sites.google.com/chromium.org/driver/

Symantec Sitereview : https://sitereview.bluecoat.com/#/
