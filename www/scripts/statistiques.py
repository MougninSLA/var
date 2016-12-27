#!/usr/bin/env python3

from mail_type_jour import * 
from mail_type_mois import *
from mail_type_annee import *
from datetime import date

print("1- Voir les statistiques d'aujourd'hui")
print("2- Voir les statistiques de chaque jour")
print("3- Voir les statistiques de chaque mois")
print("4- Voir les statistiques de chaque année")

reponse = input("Entrer un valeur : ")
if reponse == "1":
	today_all = today_mail()
	today_bon = today_bon_mail()
	today_spam = today_spam_mail()

	# On vérifie et on complète avec les dates manquantes dans les dictionaires today_bon et today_spam
	for key in today_all.keys():
		if not key in today_bon:
			today_bon[key] = 0

	for key in today_spam.keys():
		if not key in today_spam:
			today_spam[key] = 0

	if len(today) == 0:
		# On récupère la date d'aujourd'hui
		jour = date.today()
		today = str(jour.year)+"-"+str(jour.month)+"-"+str(jour.day)

		lignes, colonnes = 6, 1
		lst = [[0] * colonnes for _ in range(lignes)]

		# On remplit le tableau final avec la dates d'aujourd'hui
		h = 0
		lst[0][h] = today

		print(lst)

	else :
		lignes, colonnes = 6, len(today_all)
		lst = [[0] * colonnes for _ in range(lignes)]

		# On remplit le tableau final avec les dates et les nombres de mails
		h = 0
		s = 0
		tri = sorted(today_all)
		for g in tri:
			for key in today_all.keys():
				if g == key:
					lst[0][h] = key
					lst[1][s] = today_all[key]
					h += 1
					s += 1

		# On remplit le tableau final avec le nombre de bon mails
		h = 0
		for g in tri:
			for key in today_bon.keys():
				if g == key:
					lst[2][h] = today_bon[key]
					h += 1

		# On remplit le tableau final avec les nombres de spams
		h = 0
		for g in tri:
			for key in today_spam.keys():
				if g == key:
					lst[3][h] = today_spam[key]
					h += 1

		# On calcule et ajoute la fréquence des bon mails

		# On calcule et ajoute la fréquance des spams

		print(lst)



elif reponse == "2":	
	daily_all = daily_mail()
	daily_bon = bon_mail()
	daily_spam = spam_mail()

	# On vérifie et on complète avec les dates manquantes dans le dictionnaire
	for key in daily_all.keys():
		if not key in daily_bon:
			daily_bon[key] = 0

	for key in daily_all.keys():
		if not key in daily_spam:
			daily_spam[key] = 0

	lignes, colonnes = 6, len(daily_all)
	lst = [[0] * colonnes for _ in range(lignes)]

	# On remplit le tebleau final avec les dates et les nombres de mails
	h = 0
	s = 0
	tri = sorted(daily_all)
	for g in tri:
		for key in daily_all.keys():
			if g == key:
				lst[0][h] = key
				lst[1][s] = daily_all[key]
				h += 1
				s += 1

	# On remplit le tableau final avec les nombres de bon mails
	h = 0
	for g in tri:
		for key in daily_bon.keys():
			if g == key:
				lst[2][h] = daily_bon[key]
				h += 1

	# On remplit le tableau final avec les nombres de spams			
	h = 0
	for g in tri:
		for key in daily_spam.keys():
			if g == key:
				lst[3][h] = daily_spam[key]
				h += 1

	print(lst)
elif reponse == "3":
	monthly_all = monthly_mail()
	monthly_bon = bon_mail_mois()
	monthly_spam = spam_mail_mois()

	# On vérifie et on complète avec les dates manquantes dans le dictionnaire
	for key in monthly_all.keys():
		if not key in monthly_bon:
			monthly_bon[key] = 0

	for key in monthly_all.keys():
		if not key in monthly_spam:
			monthly_spam[key] = 0

	lignes, colonnes = 6, len(monthly_all)
	lst = [[0] * colonnes for _ in range(lignes)]

	# On remplit le tableau final avec les dates et les nombres et mails
	h = 0
	s = 0
	tri = sorted(monthly_all)
	for g in tri:
		for key in monthly_all.keys():
			if g == key:
				lst[0][h] = key
				lst[1][s] = monthly_all[key]
				h += 1
				s += 1

	# On remplit le tableau final avec les nombres de bon mails
	h = 0
	for g in tri:
		for key in monthly_bon.keys():
			if g == key:
				lst[2][h] = monthly_bon[key]
				h += 1

	# On remplit le tableau final avec les nombres de spams
	h = 0
	for g in tri:
		for key in monthly_spam.keys():
			if g == key:
				lst[3][h] = monthly_spam[key]
				h += 1

	print(lst)

elif reponse == "4":
	year_all = year_mail()
	year_bon = bon_mail_annee()
	year_spam = spam_mail_annee()

	# On vérifie et on complète avec les dates manquantes dans le dictionnaire
	for key in year_all.keys():
		if not key in year_bon:
			year_bon[key] = 0

	for key in year_all.keys():
		if not key in year_spam:
			year_spam[key] = 0

	lignes, colonnes = 6, len(year_all)
	lst = [[0] * colonnes for _ in range(lignes)]

	# On remplit le tableau final avec les années avec les nombres de mails
	h = 0
	s = 0
	tri = sorted(year_all)
	for g in tri:
		for key in year_all.keys():
			if g == key:
				lst[0][h] = key
				lst[1][s] = year_all[key]
				h +=1 
				s += 1

	# On remplit le tableau final avec les nombres de bon mails
	h = 0
	for g in tri:
		for key in year_bon.keys():
			if g == key:
				lst[2][h] = year_bon[key]
				h += 1

	# On remplit le tableau final avec les nombres de spams
	h = 0
	for g in tri:
		for key in year_spam.keys():
			lst[3][h] = year_spam[key]
			h += 1

	print(lst)

else:
	print("Entrer une valeur valide")