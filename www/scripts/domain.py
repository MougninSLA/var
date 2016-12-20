#!/usr/bin/env python3

import os, re
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
print("============================================")
print("====  Domaines  ====  Nombre de spams   ====")
print("============================================")
for key in nb_spam.keys():
	print("====  ",key,"  ====  ",nb_spam[key],"  ====")
print("============================================")