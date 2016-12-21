#!/usr/bin/env python3

from stat_spam2 import *
from mail_type_jour import * 
from mail_type_mois import *
from mail_type_annee import *
print("1- Voir les statistiques d'aujourd'hui")
print("2- Voir les statistiques de chaque jour")
print("3- Voir les statistiques de chaque mois")
print("4- Voir les statistiques de chaque année")

reponse = input("Entrer un valeur : ")
if reponse == "1":
	today_mail()
	today_bon_mail()
	today_spam_mail()
elif reponse == "2":
	daily_mail()
	bon_mail()
	spam_mail()
elif reponse == "3":
	monthly_mail()
	bon_mail_mois()
	spam_mail_mois()
elif reponse == "4":
	year_mail()
	bon_mail_annee()
	spam_mail_annee()
else:
	print("Entrer une valeur valide")