import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="domaines"
)

mycursor = mydb.cursor()

# sql_table = "CREATE TABLE `domaines` (`id` INT PRIMARY KEY AUTO_INCREMENT, `domaine` VARCHAR(100), `categorie` VARCHAR(100))"

# mycursor.execute(sql_table)

sql = "INSERT INTO domaines (`domaine`, `categorie`) VALUES (%s, %s)"

txt_files_category = [
    {
      'file' : 'DB_domaines\domains_arjel.txt',
      'category' : 'arjel'
    },
    {
      'file':'DB_domaines\domains_astrology.txt',
      'category':'astrology'
    },
    {
      'file' : 'DB_domaines\domains_agressif.txt',
      'category' : 'agressif'
    },
    {
      'file' : 'DB_domaines\domains_audio-video.txt',
      'category' : 'audio-video'
    },
    {
      'file' : 'DB_domaines\domains_bank.txt',
      'category' : 'bank'
    },
    {
      'file' : 'DB_domaines\domains_bitcoin.txt',
      'category' : 'bitcoin'
    },
    {
      'file' : 'DB_domaines\domains_celebrity.txt',
      'category' : 'celebrity'
    },
    {
      'file' : 'DB_domaines\domains_chat.txt',
      'category' : 'chat'
    },
    {
      'file' : 'DB_domaines\domains_child.txt',
      'category' : 'child'
    },
    {
      'file' : 'DB_domaines\domains_cleaning.txt',
      'category' : 'cleaning'
    },
    {
      'file' : 'DB_domaines\domains_cooking.txt',
      'category' : 'cooking'
    },
    {
      'file' : 'DB_domaines\domains_cryptojacking.txt',
      'category' : 'cryptojacking'
    },
    {
      'file' : 'DB_domaines\domains_dangerous-material.txt',
      'category' : 'dangerous-material'
    },
    {
      'file' : 'DB_domaines\domains_dating.txt',
      'category' : 'dating'
    },
    {
      'file' : 'DB_domaines\domains_ddos.txt',
      'category' : 'ddos'
    },
    {
      'file' : 'DB_domaines\domains_dialer.txt',
      'category' : 'dialer'
    },
    {
      'file' : 'DB_domaines\domains_doh.txt',
      'category' : 'doh'
    },
    {
      'file' : 'DB_domaines\domains_download.txt',
      'category' : 'download'
    },
    {
      'file' : 'DB_domaines\domains_drogue.txt',
      'category' : 'drogue'
    },
    {
      'file' : 'DB_domaines\domains_education-games.txt',
      'category' : 'education-games'
    },
    {
      'file' : 'DB_domaines\domains_examen_pix.txt',
      'category' : 'examen-pix'
    },
    {
      'file' : 'DB_domaines\domains_file-hosting.txt',
      'category' : 'file-hosting'
    },
    {
      'file' : 'DB_domaines\domains_financial.txt',
      'category' : 'financial'
    },
    {
      'file' : 'DB_domaines\domains_forum.txt',
      'category' : 'forum'
    },
    {
      'file' : 'DB_domaines\domains_gambling.txt',
      'category' : 'gambling'
    },
    {
      'file' : 'DB_domaines\domains_games.txt',
      'category' : 'games'
    },

    {
      'file' : 'DB_domaines\domains_hacking.txt',
      'category' : 'hacking'
    },
    {
      'file' : 'DB_domaines\domains_indisponible.txt',
      'category' : 'indisponible'
    },
    {
      'file' : 'DB_domaines\domains_jobsearch.txt',
      'category' : 'jobsearch'
    },
    {
      'file' : 'DB_domaines\domains_jstor.txt',
      'category' : 'jstor'
    },
    {
      'file' : 'DB_domaines\domains_lingerie.txt',
      'category' : 'lingerie'
    },
    {
      'file' : 'DB_domaines\domains_liste-blanche.txt',
      'category' : 'liste-blanche'
    },
    {
      'file' : 'DB_domaines\domains_liste-bu.txt',
      'category' : 'liste-bu'
    },
    {
      'file' : 'DB_domaines\domains_local.txt',
      'category' : 'local'
    },
    {
      'file' : 'DB_domaines\domains_manga.txt',
      'category' : 'manga'
    },
    {
      'file' : 'DB_domaines\domains_marketingware.txt',
      'category' : 'marketingware'
    },
    {
      'file' : 'DB_domaines\domains_mixed-adult.txt',
      'category' : 'mixed_adult'
    },
    {
      'file' : 'DB_domaines\domains_mobile_phone.txt',
      'category' : 'mobile_phone'
    },
    {
      'file' : 'DB_domaines\domains_phising.txt',
      'category' : 'phising'
    },
    {
      'file' : 'DB_domaines\domains_press.txt',
      'category' : 'press'
    },
    {
      'file' : 'DB_domaines\domains_publicite.txt',
      'category' : 'publicite'
    },
    {
      'file' : 'DB_domaines\domains_radio.txt',
      'category' : 'radio'
    },
    {
      'file' : 'DB_domaines\domains_reaffected.txt',
      'category' : 'reaffected'
    },
    {
      'file' : 'DB_domaines\domains_redirector.txt',
      'category' : 'redirector'
    },
    {
      'file' : 'DB_domaines\domains_religieuses.txt',
      'category' : 'religieuse'
    },
    {
      'file' : 'DB_domaines\domains_remote-control.txt',
      'category' : 'remote-control'
    },
    {
      'file' : 'DB_domaines\domains_sect.txt',
      'category' : 'sect'
    },
    {
      'file' : 'DB_domaines\domains_sexual-education.txt',
      'category' : 'sexual-education'
    },
    {
      'file' : 'DB_domaines\domains_shopping.txt',
      'category' : 'shopping'
    },
    {
      'file' : 'DB_domaines\domains_shortener.txt',
      'category' : 'shortener'
    },
    {
      'file' : 'DB_domaines\domains_social-network.txt',
      'category' : 'social-network'
    },
    {
      'file' : 'DB_domaines\domains_special.txt',
      'category' : 'special'
    },
    {
      'file' : 'DB_domaines\domains_sports.txt',
      'category' : 'sports'
    },
    {
      'file' : 'DB_domaines\domains_stalkerware.txt',
      'category' : 'stalkeware'
    },
    {
      'file' : 'DB_domaines\domains_strict-redirector.txt',
      'category' : 'strict-redirector'
    },
    {
      'file' : 'DB_domaines\domains_translation.txt',
      'category' : 'translation'
    },
    {
      'file' : 'DB_domaines\domains_tricheur.txt',
      'category' : 'tricheur'
    },
    {
      'file' : 'DB_domaines\domains_update.txt',
      'category' : 'update'
    },
    {
      'file' : 'DB_domaines\domains_verisign.txt',
      'category' : 'verisign'
    },
    {
      'file' : 'DB_domaines\domains_vpn.txt',
      'category' : 'vpn'
    },
    {
      'file' : 'DB_domaines\domains_warez.txt',
      'category' : 'warez'
    },
    {
      'file' : 'DB_domaines\domains_webmail.txt',
      'category' : 'webmail'
    },
    {
      'file' : 'DB_domaines\domains_adult.txt',
      'category' : 'adult'
    }
]

for i in range(len(txt_files_category)):
  domaine_txt = open(txt_files_category[i]['file'])
  for lines in domaine_txt:
    lignes = lines[:-1]
    print(lignes)
    val = (lignes, txt_files_category[i]['category'])
    mycursor.execute(sql, val)
  i += 1

mydb.commit()