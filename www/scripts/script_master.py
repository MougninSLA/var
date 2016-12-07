#!/usr/bin/env python3

import os
from subprocess import Popen
reponse = "oui"

while reponse == "oui" :
	os.system('clear')
	print("""Bienvenue sur la plate-forme d'administration SYM
	Que souhaitez-vous faire ?
	1- Ajouter une adresse mail dans la blacklist
	2- Retirer une adresse mail de la blacklist
	3- Ajouter un domaine dans la blacklist
	4- Retirer un domaine de la blacklist
	5- Ajouter un domaine dans la whitelist
	6- Retirer un domaine de la whitelist
	7- Modifier le timer du tarpit
	8- Créer un compte mail
	9- Fermer un compte mail""")
	
	print(" ")
	choix = input("Entrez votre choix : ")
	if choix == "1" :
		adress = input("Entrez l'adresse cible : ")
		os.system("sh /var/www/scripts/add_blacklist.sh "+ adress)
	elif choix == "2" :
		adress = input("Entrez l'adress cible : ")
		os.system("sh /var/www/scripts/rm_blacklist.sh "+ adress)
	elif choix == "3" :
		domain = input("Entrez le domaine cible : ")
		os.system("sh /var/www/scripts/add_blacklist.sh "+ "@"+domain)
	elif choix == "4" :
		domain = input("Entrez le domaine cible : ")
		os.system("sh /var/www/scripts/rm_blacklist.sh "+ "@"+domain)
	elif choix == "5" :
		domain = input("Entrez le domaine cible : ")
		os.system("sh /var/www/scripts/add_whitelist.sh "+ domain)
	elif choix == "6" :
		domain = input("Entrez le domaine cible : ")
		os.system("sh /var/www/scripts/rm_whitelist.sh "+ domain)
	elif choix == "7" :
		time = input("Donnez la durée du tarpit(en seconde) : ")
		os.system("perl /var/www/scripts/tarpit_time.pl "+ time)
	elif choix == "8" :
		compte = input("Entrez le nom du compte : ")
		mdp = input("Entrez le mot de passe : ")
		Popen(['ssh', '-i', '/root/.ssh/id_rsa_add', 'root@10.8.102.195', compte +' '+ mdp])
	elif choix == "9" :
		compte = input("Entrez le nom du compte : ")
		Popen(['ssh', '-i', '/root/.ssh/id_rsa_del', 'root@10.8.102.195', compte])	
	else :
		print("Veuillez entrer l'une des propositions ci-dessus !")
	reponse = input("Voulez-vous continuer ? oui/non ")
