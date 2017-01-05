#!/usr/bin/env python3

import os, re, mysql.connector 

conn = mysql.connector.connect(host="localhost",user="root",password="africainetfier", database="sym")
cursor = conn.cursor()

domaines = []
os.system("ls /var/spool/sa-exim/SAteergrube/new/ > /var/www/scripts/domaine")
fichier = open("/var/www/scripts/domaine", "r")
for ligne in fichier:	
	# On supprime le \n qui se trouve à la fin de la ligne
	ligne = ligne.rstrip('\n')
	f = open("/var/spool/sa-exim/SAteergrube/new/"+ligne, "r")
	# On récupère la première ligne des fichiers de spams
	while 1:
		data = f.readline()
		if data:
			data = re.findall("([a-z0-9._-]+@[a-z0-9._-]+\.[(com|fr)]+)", data)
			for i in data:
				i = i.split("@")
				domaine = i[1] 
			break
	f.close()
	domaines.append(domaine)
fichier.close()

nb_spam = {}
while domaines:
	nb = domaines.count(domaines[0])
	nb_spam[domaines[0]] = nb
	i = domaines[0]
	domaines = [y for y in domaines if y != i]
#print(nb_spam)

requete = ("SELECT nom_spamers FROM domains_spamers;")
cursor.execute(requete)
rows = cursor.fetchall()

domains = []
for row in rows:
	domains.append("{0}".format(row[0]))

for key in nb_spam.keys():
	if not key in domains:
		requete = ("INSERT INTO domains_spamers (nom_spamers, nb_spams) VALUES (%s, %s)")
		data_requete = (key, nb_spam[key])
		cursor.execute(requete, data_requete)
	else:
		requete = ("UPDATE domains_spamers SET nb_spams = %s WHERE nom_spamers = %s")
		cursor.execute(requete, (nb_spam[key], key))
conn.commit()

conn.close()