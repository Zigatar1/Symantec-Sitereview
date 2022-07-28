domaines_sql_database = open('base_de_données.txt','w')

domaines_sql_database.write("CREATE DATABASE domaines,\n")

domaines_adult_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_adult.txt', "r")

domaines_sql_database.write("CREATE TABLE adult(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO adult(domaine, categorie) VALUES\n")

for lines in domaines_adult_txt:
    lignes = lines[:-1]
    adult_sql = lignes,"adult"
    domaines_sql_database.write(str(adult_sql)+",\n")

domaines_adult_txt.close()

domaines_arjel_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_arjel.txt', "r")

domaines_sql_database.write("CREATE TABLE arjel(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO arjel(domaine, categorie) VALUES\n")

for lines in domaines_arjel_txt:
    lignes = lines[:-1]
    arjel_sql = lignes,"arjel"
    domaines_sql_database.write(str(arjel_sql)+",\n")

domaines_arjel_txt.close()

domaines_agressif_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_agressif.txt', "r")

domaines_sql_database.write("CREATE TABLE agressif(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO agressif(domaine, categorie) VALUES\n")

for lines in domaines_agressif_txt:
    lignes = lines[:-1]
    agressif_sql = lignes,"agressif"
    domaines_sql_database.write(str(agressif_sql)+",\n")

domaines_agressif_txt.close()

domaines_astrology_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_astrology.txt', "r")

domaines_sql_database.write("CREATE TABLE astrology(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO astrology(domaine, categorie) VALUES\n")

for lines in domaines_astrology_txt:
    lignes = lines[:-1]
    astrology_sql = lignes,"astrology"
    domaines_sql_database.write(str(astrology_sql)+",\n")

domaines_astrology_txt.close()

domaines_audiovideo_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_audio-video.txt', "r")

domaines_sql_database.write("CREATE TABLE audiovideo(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO audiovideo(domaine, categorie) VALUES\n")

for lines in domaines_audiovideo_txt:
    lignes = lines[:-1]
    audiovideo_sql = lignes,"audiovideo"
    domaines_sql_database.write(str(audiovideo_sql)+",\n")

domaines_audiovideo_txt.close()

domaines_bank_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_bank.txt', "r")

domaines_sql_database.write("CREATE TABLE bank(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO bank(domaine, categorie) VALUES\n")

for lines in domaines_bank_txt:
    lignes = lines[:-1]
    bank_sql = lignes,"bank"
    domaines_sql_database.write(str(bank_sql)+",\n")

domaines_bank_txt.close()

domaines_bitcoin_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_bitcoin.txt', "r")

domaines_sql_database.write("CREATE TABLE bitcoin(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO bitcoin(domaine, categorie) VALUES\n")

for lines in domaines_bitcoin_txt:
    lignes = lines[:-1]
    bitcoin_sql = lignes,"bitcoin"
    domaines_sql_database.write(str(bitcoin_sql)+",\n")

domaines_bitcoin_txt.close()

domaines_celebrity_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_celebrity.txt', "r")

domaines_sql_database.write("CREATE TABLE celebrity(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO celebrity(domaine, categorie) VALUES\n")

for lines in domaines_celebrity_txt:
    lignes = lines[:-1]
    celebrity_sql = lignes,"celebrity"
    domaines_sql_database.write(str(celebrity_sql)+",\n")

domaines_celebrity_txt.close()

domaines_chat_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_chat.txt', "r")

domaines_sql_database.write("CREATE TABLE chat(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO chat(domaine, categorie) VALUES\n")

for lines in domaines_chat_txt:
    lignes = lines[:-1]
    chat_sql = lignes,"chat"
    domaines_sql_database.write(str(chat_sql)+",\n")

domaines_chat_txt.close()

domaines_child_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_child.txt', "r")

domaines_sql_database.write("CREATE TABLE child(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO child(domaine, categorie) VALUES\n")

for lines in domaines_child_txt:
    lignes = lines[:-1]
    child_sql = lignes,"child"
    domaines_sql_database.write(str(child_sql)+",\n")

domaines_child_txt.close()

domaines_cleaning_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_cleaning.txt', "r")

domaines_sql_database.write("CREATE TABLE cleaning(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO cleaning(domaine, categorie) VALUES\n")

for lines in domaines_cleaning_txt:
    lignes = lines[:-1]
    cleaning_sql = lignes,"cleaning"
    domaines_sql_database.write(str(cleaning_sql)+",\n")

domaines_cleaning_txt.close()

domaines_cooking_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_cooking.txt', "r")

domaines_sql_database.write("CREATE TABLE cooking(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO cooking(domaine, categorie) VALUES\n")

for lines in domaines_cooking_txt:
    lignes = lines[:-1]
    cooking_sql = lignes,"cooking"
    domaines_sql_database.write(str(cooking_sql)+",\n")

domaines_cooking_txt.close()

domaines_cryptojacking_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_cryptojacking.txt', "r")

domaines_sql_database.write("CREATE TABLE cryptojacking(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO cryptojacking(domaine, categorie) VALUES\n")

for lines in domaines_cryptojacking_txt:
    lignes = lines[:-1]
    cryptojacking_sql = lignes,"cryptojacking"
    domaines_sql_database.write(str(cryptojacking_sql)+",\n")

domaines_cryptojacking_txt.close()

domaines_dangerousmaterial_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_dangerous-material.txt', "r")

domaines_sql_database.write("CREATE TABLE dangerousmaterial(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO dangerousmaterial(domaine, categorie) VALUES\n")

for lines in domaines_dangerousmaterial_txt:
    lignes = lines[:-1]
    dangerousmaterial_sql = lignes,"dangerous-material"
    domaines_sql_database.write(str(dangerousmaterial_sql)+",\n")

domaines_dangerousmaterial_txt.close()

domaines_dating_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_dating.txt', "r")

domaines_sql_database.write("CREATE TABLE dating(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO dating(domaine, categorie) VALUES\n")

for lines in domaines_dating_txt:
    lignes = lines[:-1]
    dating_sql = lignes,"dating"
    domaines_sql_database.write(str(dating_sql)+",\n")

domaines_dating_txt.close()

domaines_ddos_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_ddos.txt', "r")

domaines_sql_database.write("CREATE TABLE ddos(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO ddos(domaine, categorie) VALUES\n")

for lines in domaines_ddos_txt:
    lignes = lines[:-1]
    ddos_sql = lignes,"ddos"
    domaines_sql_database.write(str(ddos_sql)+",\n")

domaines_ddos_txt.close()

domaines_doh_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_doh.txt', "r")

domaines_sql_database.write("CREATE TABLE doh(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO doh(domaine, categorie) VALUES\n")

for lines in domaines_doh_txt:
    lignes = lines[:-1]
    doh_sql = lignes,"doh"
    domaines_sql_database.write(str(doh_sql)+",\n")

domaines_doh_txt.close()

domaines_download_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_download.txt', "r")

domaines_sql_database.write("CREATE TABLE download(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO download(domaine, categorie) VALUES\n")

for lines in domaines_download_txt:
    lignes = lines[:-1]
    download_sql = lignes,"download"
    domaines_sql_database.write(str(download_sql)+",\n")

domaines_download_txt.close()

domaines_drogue_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_drogue.txt', "r")

domaines_sql_database.write("CREATE TABLE drogue(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO drogue(domaine, categorie) VALUES\n")

for lines in domaines_drogue_txt:
    lignes = lines[:-1]
    drogue_sql = lignes,"drogue"
    domaines_sql_database.write(str(drogue_sql)+",\n")

domaines_drogue_txt.close()

domaines_educationgames_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_education-games.txt', "r")

domaines_sql_database.write("CREATE TABLE educationgames(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO educationgames(domaine, categorie) VALUES\n")

for lines in domaines_educationgames_txt:
    lignes = lines[:-1]
    educationgames_sql = lignes,"education games"
    domaines_sql_database.write(str(educationgames_sql)+",\n")

domaines_educationgames_txt.close()

domaines_examen_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_examen_pix.txt', "r")

domaines_sql_database.write("CREATE TABLE examen_pix(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO examen_pix(domaine, categorie) VALUES\n")

for lines in domaines_examen_txt:
    lignes = lines[:-1]
    examen_sql = lignes,"examen pix"
    domaines_sql_database.write(str(examen_sql)+",\n")

domaines_examen_txt.close()

domaines_filehosting_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_file-hosting.txt', "r")

domaines_sql_database.write("CREATE TABLE filehosting(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO filehosting(domaine, categorie) VALUES\n")

for lines in domaines_filehosting_txt:
    lignes = lines[:-1]
    filehosting_sql = lignes,"file hosting"
    domaines_sql_database.write(str(filehosting_sql)+",\n")

domaines_filehosting_txt.close()

domaines_financial_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_financial.txt', "r")

domaines_sql_database.write("CREATE TABLE financial(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO financial(domaine, categorie) VALUES\n")

for lines in domaines_financial_txt:
    lignes = lines[:-1]
    financial_sql = lignes,"financial"
    domaines_sql_database.write(str(financial_sql)+",\n")

domaines_financial_txt.close()

domaines_forum_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_forum.txt', "r")

domaines_sql_database.write("CREATE TABLE forum(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO forum(domaine, categorie) VALUES\n")

for lines in domaines_forum_txt:
    lignes = lines[:-1]
    forum_sql = lignes,"forum"
    domaines_sql_database.write(str(forum_sql)+",\n")

domaines_forum_txt.close()

domaines_gambling_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_gambling.txt', "r")

domaines_sql_database.write("CREATE TABLE gambling(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO gambling(domaine, categorie) VALUES\n")

for lines in domaines_gambling_txt:
    lignes = lines[:-1]
    gambling_sql = lignes,"gambling"
    domaines_sql_database.write(str(gambling_sql)+",\n")

domaines_gambling_txt.close()

domaines_gambling_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_gambling.txt', "r")

domaines_sql_database.write("CREATE TABLE gambling(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO gambling(domaine, categorie) VALUES\n")

for lines in domaines_gambling_txt:
    lignes = lines[:-1]
    gambling_sql = lignes,"gambling"
    domaines_sql_database.write(str(gambling_sql)+",\n")

domaines_gambling_txt.close()

domaines_games_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_games.txt', "r")

domaines_sql_database.write("CREATE TABLE games(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO games(domaine, categorie) VALUES\n")

for lines in domaines_games_txt:
    lignes = lines[:-1]
    games_sql = lignes,"games"
    domaines_sql_database.write(str(games_sql)+",\n")

domaines_games_txt.close()

domaines_hacking_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_hacking.txt', "r")

domaines_sql_database.write("CREATE TABLE hacking(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO hacking(domaine, categorie) VALUES\n")

for lines in domaines_hacking_txt:
    lignes = lines[:-1]
    hacking_sql = lignes,"hacking"
    domaines_sql_database.write(str(hacking_sql)+",\n")

domaines_hacking_txt.close()

domaines_indisponible_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_indisponible.txt', "r")

domaines_sql_database.write("CREATE TABLE indisponible(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO indisponible(domaine, categorie) VALUES\n")

for lines in domaines_indisponible_txt:
    lignes = lines[:-1]
    indisponible_sql = lignes,"indisponible"
    domaines_sql_database.write(str(indisponible_sql)+",\n")

domaines_indisponible_txt.close()

domaines_jobsearch_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_jobsearch.txt', "r")

domaines_sql_database.write("CREATE TABLE jobsearch(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO jobsearch(domaine, categorie) VALUES\n")

for lines in domaines_jobsearch_txt:
    lignes = lines[:-1]
    jobsearch_sql = lignes,"jobsearch"
    domaines_sql_database.write(str(jobsearch_sql)+",\n")

domaines_jobsearch_txt.close()

domaines_lingerie_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_lingerie.txt', "r")

domaines_sql_database.write("CREATE TABLE lingerie(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO lingerie(domaine, categorie) VALUES\n")

for lines in domaines_lingerie_txt:
    lignes = lines[:-1]
    lingerie_sql = lignes,"lingerie"
    domaines_sql_database.write(str(lingerie_sql)+",\n")

domaines_lingerie_txt.close()

domaines_listeblanche_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_liste-blanche.txt', "r")

domaines_sql_database.write("CREATE TABLE listeblanche(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO listeblanche(domaine, categorie) VALUES\n")

for lines in domaines_listeblanche_txt:
    lignes = lines[:-1]
    listeblanche_sql = lignes,"liste blanche"
    domaines_sql_database.write(str(listeblanche_sql)+",\n")

domaines_listeblanche_txt.close()

domaines_listebu_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_liste-bu.txt', "r")

domaines_sql_database.write("CREATE TABLE listebu(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO listebu(domaine, categorie) VALUES\n")

for lines in domaines_listebu_txt:
    lignes = lines[:-1]
    listebu_sql = lignes,"liste bu"
    domaines_sql_database.write(str(listebu_sql)+",\n")

domaines_listebu_txt.close()

domaines_manga_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_manga.txt', "r")

domaines_sql_database.write("CREATE TABLE manga(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO manga(domaine, categorie) VALUES\n")

for lines in domaines_manga_txt:
    lignes = lines[:-1]
    manga_sql = lignes,"manga"
    domaines_sql_database.write(str(manga_sql)+",\n")

domaines_manga_txt.close()

domaines_marketingware_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_marketingware.txt', "r")

domaines_sql_database.write("CREATE TABLE marketingware(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO marketingware(domaine, categorie) VALUES\n")

for lines in domaines_marketingware_txt:
    lignes = lines[:-1]
    marketingware_sql = lignes,"marketingware"
    domaines_sql_database.write(str(marketingware_sql)+",\n")

domaines_marketingware_txt.close()

domaines_mixedadult_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_mixed-adult.txt', "r")

domaines_sql_database.write("CREATE TABLE mixedadult(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO mixedadult(domaine, categorie) VALUES\n")

for lines in domaines_mixedadult_txt:
    lignes = lines[:-1]
    mixedadult_sql = lignes,"mixed adult"
    domaines_sql_database.write(str(mixedadult_sql)+",\n")

domaines_mixedadult_txt.close()

domaines_mobilephone_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_mobile_phone.txt', "r")

domaines_sql_database.write("CREATE TABLE mobilephone(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO mobilephone(domaine, categorie) VALUES\n")

for lines in domaines_mobilephone_txt:
    lignes = lines[:-1]
    mobilephone_sql = lignes,"mobile phone"
    domaines_sql_database.write(str(mobilephone_sql)+",\n")

domaines_mobilephone_txt.close()

domaines_phising_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_phising.txt', "r")

domaines_sql_database.write("CREATE TABLE phising(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO phising(domaine, categorie) VALUES\n")

for lines in domaines_phising_txt:
    lignes = lines[:-1]
    phising_sql = lignes,"phising"
    domaines_sql_database.write(str(phising_sql)+",\n")

domaines_phising_txt.close()

domaines_press_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_press.txt', "r")

domaines_sql_database.write("CREATE TABLE press(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO press(domaine, categorie) VALUES\n")

for lines in domaines_press_txt:
    lignes = lines[:-1]
    press_sql = lignes,"press"
    domaines_sql_database.write(str(press_sql)+",\n")

domaines_press_txt.close()

domaines_publicite_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_publicite.txt', "r")

domaines_sql_database.write("CREATE TABLE publicite(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO publicite(domaine, categorie) VALUES\n")

for lines in domaines_publicite_txt:
    lignes = lines[:-1]
    publicite_sql = lignes,"publicite"
    domaines_sql_database.write(str(publicite_sql)+",\n")

domaines_publicite_txt.close()

domaines_radio_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_radio.txt', "r")

domaines_sql_database.write("CREATE TABLE radio(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO radio(domaine, categorie) VALUES\n")

for lines in domaines_radio_txt:
    lignes = lines[:-1]
    radio_sql = lignes,"radio"
    domaines_sql_database.write(str(radio_sql)+",\n")

domaines_radio_txt.close()

domaines_reaffected_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_reaffected.txt', "r")

domaines_sql_database.write("CREATE TABLE reaffected(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO reaffected(domaine, categorie) VALUES\n")

for lines in domaines_reaffected_txt:
    lignes = lines[:-1]
    reaffected_sql = lignes,"reaffected"
    domaines_sql_database.write(str(reaffected_sql)+",\n")

domaines_reaffected_txt.close()

domaines_redirector_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_redirector.txt', "r")

domaines_sql_database.write("CREATE TABLE redirector(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO redirector(domaine, categorie) VALUES\n")

for lines in domaines_redirector_txt:
    lignes = lines[:-1]
    redirector_sql = lignes,"redirector"
    domaines_sql_database.write(str(redirector_sql)+",\n")

domaines_redirector_txt.close()

domaines_religieuse_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_religieuses.txt', "r")

domaines_sql_database.write("CREATE TABLE religieuse(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO religieuse(domaine, categorie) VALUES\n")

for lines in domaines_religieuse_txt:
    lignes = lines[:-1]
    religieuse_sql = lignes,"religieuse"
    domaines_sql_database.write(str(religieuse_sql)+",\n")

domaines_religieuse_txt.close()

domaines_remotecontrol_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_remote-control.txt', "r")

domaines_sql_database.write("CREATE TABLE remotecontrol(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO remotecontrol(domaine, categorie) VALUES\n")

for lines in domaines_remotecontrol_txt:
    lignes = lines[:-1]
    remotecontrol_sql = lignes,"remote control"
    domaines_sql_database.write(str(remotecontrol_sql)+",\n")

domaines_remotecontrol_txt.close()

domaines_sect_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_sect.txt', "r")

domaines_sql_database.write("CREATE TABLE sect(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO sect(domaine, categorie) VALUES\n")

for lines in domaines_sect_txt:
    lignes = lines[:-1]
    sect_sql = lignes,"sect"
    domaines_sql_database.write(str(sect_sql)+",\n")

domaines_sect_txt.close()

domaines_sexualeducation_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_sexual-education.txt', "r")

domaines_sql_database.write("CREATE TABLE sexualeducation(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO sexualeducation(domaine, categorie) VALUES\n")

for lines in domaines_sexualeducation_txt:
    lignes = lines[:-1]
    sexualeducation_sql = lignes,"sexual education"
    domaines_sql_database.write(str(sexualeducation_sql)+",\n")

domaines_sexualeducation_txt.close()

domaines_shopping_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_shopping.txt', "r")

domaines_sql_database.write("CREATE TABLE shopping(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO shopping(domaine, categorie) VALUES\n")

for lines in domaines_shopping_txt:
    lignes = lines[:-1]
    shopping_sql = lignes,"shopping"
    domaines_sql_database.write(str(shopping_sql)+",\n")

domaines_shopping_txt.close()

domaines_shortener_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_shortener.txt', "r")

domaines_sql_database.write("CREATE TABLE shortener(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO shortener(domaine, categorie) VALUES\n")

for lines in domaines_shortener_txt:
    lignes = lines[:-1]
    shortener_sql = lignes,"shortener"
    domaines_sql_database.write(str(shortener_sql)+",\n")

domaines_shortener_txt.close()

domaines_socialnetwork_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_social-network.txt', "r")

domaines_sql_database.write("CREATE TABLE socialnetwork(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO socialnetwork(domaine, categorie) VALUES\n")

for lines in domaines_socialnetwork_txt:
    lignes = lines[:-1]
    socialnetwork_sql = lignes,"socialnetwork"
    domaines_sql_database.write(str(socialnetwork_sql)+",\n")

domaines_socialnetwork_txt.close()

domaines_special_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_special.txt', "r")

domaines_sql_database.write("CREATE TABLE special(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO special(domaine, categorie) VALUES\n")

for lines in domaines_special_txt:
    lignes = lines[:-1]
    special_sql = lignes,"special"
    domaines_sql_database.write(str(special_sql)+",\n")

domaines_special_txt.close()

domaines_sports_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_sports.txt', "r")

domaines_sql_database.write("CREATE TABLE sports(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO sports(domaine, categorie) VALUES\n")

for lines in domaines_sports_txt:
    lignes = lines[:-1]
    sports_sql = lignes,"sports"
    domaines_sql_database.write(str(sports_sql)+",\n")

domaines_sports_txt.close()

domaines_stalkerware_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_stalkerware.txt', "r")

domaines_sql_database.write("CREATE TABLE stalkerware(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO stalkerware(domaine, categorie) VALUES\n")

for lines in domaines_stalkerware_txt:
    lignes = lines[:-1]
    stalkerware_sql = lignes,"stalkerware"
    domaines_sql_database.write(str(stalkerware_sql)+",\n")

domaines_stalkerware_txt.close()

domaines_strictredirector_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_strict-redirector.txt', "r")

domaines_sql_database.write("CREATE TABLE strictredirector(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO strictredirector(domaine, categorie) VALUES\n")

for lines in domaines_strictredirector_txt:
    lignes = lines[:-1]
    strictredirector_sql = lignes,"strict redirector"
    domaines_sql_database.write(str(strictredirector_sql)+",\n")

domaines_strictredirector_txt.close()

domaines_strongredirector_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_strong-redirector.txt', "r")

domaines_sql_database.write("CREATE TABLE strongredirector(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO strongredirector(domaine, categorie) VALUES\n")

for lines in domaines_strongredirector_txt:
    lignes = lines[:-1]
    strongredirector_sql = lignes,"strong redirector"
    domaines_sql_database.write(str(strongredirector_sql)+",\n")

domaines_strongredirector_txt.close()

domaines_translation_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_translation.txt', "r")

domaines_sql_database.write("CREATE TABLE translation(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO translation(domaine, categorie) VALUES\n")

for lines in domaines_translation_txt:
    lignes = lines[:-1]
    translation_sql = lignes,"translation"
    domaines_sql_database.write(str(translation_sql)+",\n")

domaines_translation_txt.close()

domaines_tricheur_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_tricheur.txt', "r")

domaines_sql_database.write("CREATE TABLE tricheur(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO tricheur(domaine, categorie) VALUES\n")

for lines in domaines_tricheur_txt:
    lignes = lines[:-1]
    tricheur_sql = lignes,"tricheur"
    domaines_sql_database.write(str(tricheur_sql)+",\n")

domaines_tricheur_txt.close()

domaines_update_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_update.txt', "r")

domaines_sql_database.write("CREATE TABLE update(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO update(domaine, categorie) VALUES\n")

for lines in domaines_update_txt:
    lignes = lines[:-1]
    update_sql = lignes,"update"
    domaines_sql_database.write(str(update_sql)+",\n")

domaines_update_txt.close()

domaines_verisign_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_verisign.txt', "r")

domaines_sql_database.write("CREATE TABLE verisign(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO verisign(domaine, categorie) VALUES\n")

for lines in domaines_verisign_txt:
    lignes = lines[:-1]
    verisign_sql = lignes,"verisign"
    domaines_sql_database.write(str(verisign_sql)+",\n")

domaines_verisign_txt.close()

domaines_vpn_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_vpn.txt', "r")

domaines_sql_database.write("CREATE TABLE vpn(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO vpn(domaine, categorie) VALUES\n")

for lines in domaines_vpn_txt:
    lignes = lines[:-1]
    vpn_sql = lignes,"vpn"
    domaines_sql_database.write(str(vpn_sql)+",\n")

domaines_vpn_txt.close()

domaines_warez_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_warez.txt', "r")

domaines_sql_database.write("CREATE TABLE warez(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO warez(domaine, categorie) VALUES\n")

for lines in domaines_warez_txt:
    lignes = lines[:-1]
    warez_sql = lignes,"warez"
    domaines_sql_database.write(str(warez_sql)+",\n")

domaines_warez_txt.close()

domaines_webmail_txt = open('E:\Projet Historique Navigation\DB_domaines\domains_webmail.txt', "r")

domaines_sql_database.write("CREATE TABLE webmail(id INTEGER PRIMARY KEY AUTO_INCREMENT, domaine VARCHAR(100), categorie VARCHAR(100)),\n")

domaines_sql_database.write("INSERT INTO webmail(domaine, categorie) VALUES\n")

for lines in domaines_webmail_txt:
    lignes = lines[:-1]
    webmail_sql = lignes,"webmail"
    domaines_sql_database.write(str(webmail_sql)+",\n")

domaines_webmail_txt.close()

domaines_sql_database.close()