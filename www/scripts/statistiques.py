#!/usr/bin/env python3

from mail_type_jour import * 
from mail_type_mois import *
from mail_type_annee import *
from datetime import date
import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="africainetfier", database="test1")
cursor = conn.cursor()

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

	if len(today_all) == 0:
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
				# On effectue le calcule des fréquences pour les bons mails
				lst[4][h] = (round(lst[2][h] / lst[1][h],2)) * 100 
				h += 1

	# On remplit le tableau final avec les nombres de spams			
	h = 0
	for g in tri:
		for key in daily_spam.keys():
			if g == key:
				lst[3][h] = daily_spam[key]
				# On effectue le calcule des fréquences pour les spams mails
				lst[5][h] = (round(lst[3][h] / lst[1][h],2)) * 100
				h += 1

	#print(lst)

	j = 0
	#while i < 6:
	requete_jour = "SELECT jours FROM mails_journaliers;"
	cursor.execute(requete_jour)
	rows = cursor.fetchall()
	jours = []
	for row in rows:
		jours.append("{0}".format(row[0]))

	while j < len(daily_all):
		if not lst[0][j] in jours:
			print("Chaque ligne ",j," du tableau")
			print(lst[0][j]," ",lst[1][j]," ",lst[2][j]," ",lst[3][j]," ",lst[4][j]," ",lst[5][j])
			requete=("INSERT INTO mails_journaliers (jours, mails_totaux, bon_mails, spam_mails, frequence_bon_mails, frequence_spam_mails) VALUES (%s, %s, %s, %s, %s, %s)")
			data_requete = (lst[0][j], lst[1][j], lst[2][j], lst[3][j], lst[4][j], lst[5][j])
			cursor.execute(requete, data_requete)
		else:
			requete = ("UPDATE mails_journaliers SET mails_totaux = %s, bon_mails = %s, spam_mails = %s, frequence_bon_mails = %s, frequence_spam_mails = %s WHERE jours = %s")
			cursor.execute(requete, (lst[1][j], lst[2][j], lst[3][j], lst[4][j], lst[5][j], lst[0][j]))
		j += 1
	conn.commit()
		
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
				# On calcule la fréquence de bon mails
				lst[4][h] = (round(lst[2][h] / lst[1][h],2)) * 100
				h += 1

	# On remplit le tableau final avec les nombres de spams
	h = 0
	for g in tri:
		for key in monthly_spam.keys():
			if g == key:
				lst[3][h] = monthly_spam[key]
				# On calcule la fréquence des spams
				lst[5][h] = (round(lst[3][h] / lst[1][h],2)) * 100
				h += 1

	#print(lst)

	j = 0

	requete_mois = "SELECT mois FROM mails_mensuels;"
	cursor.execute(requete_mois)
	rows = cursor.fetchall()
	mois = []
	for row in rows:
		mois.append("{0}".format(row[0]))

	while j < len(monthly_all):
		if not lst[0][j] in mois:
			print("Chaque ligne ",j," du tableau")
			print(lst[0][j]," ",lst[1][j]," ",lst[2][j]," ",lst[3][j]," ",lst[4][j]," ",lst[5][j])
			requete = ("INSERT INTO mails_mensuels (mois, mails_totaux, bon_mails, spam_mails, frequence_bon_mails, frequence_spam_mails) VALUES (%s, %s, %s, %s, %s, %s)")
			data_requete = (lst[0][j], lst[1][j], lst[2][j], lst[3][j], lst[4][j], lst[5][j])
			cursor.execute(requete, data_requete)
		else:
			requete = ("UPDATE mails_mensuels SET mails_totaux = %s, bon_mails = %s, spam_mails = %s, frequence_bon_mails = %s, frequence_spam_mails = %s WHERE mois = %s")
			cursor.execute(requete, (lst[1][j], lst[2][j], lst[3][j], lst[4][j], lst[5][j], lst[0][j]))
		j += 1
	conn.commit()

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
				# On calcule la fréquence des bon mails
				lst[4][h] = (round(lst[2][h] / lst[1][h],2)) * 100
				h += 1

	# On remplit le tableau final avec les nombres de spams
	h = 0
	for g in tri:
		for key in year_spam.keys():
			if g == key:
				lst[3][h] = year_spam[key]
				# On calcule la fréquence des spams
				lst[5][h] = (round(lst[3][h] / lst[1][h],2)) * 100
				h += 1

	#print(lst)

	j = 0

	requete_annees = "SELECT annee FROM mails_annuels;"
	cursor.execute(requete_annees)
	rows = cursor.fetchall()
	annees = []
	for row in rows:
		annees.append("{0}".format(row[0]))

	while j < len(year_all):
		if not lst[0][j] in annees:
			print("Chaque ligne ",j," du tableau")
			print(lst[0][j]," ",lst[1][j]," ",lst[2][j]," ",lst[3][j]," ",lst[4][j]," ",lst[5][j])
			requete = ("INSERT INTO mails_annuels (annee, mails_totaux, bon_mails, spam_mails, frequence_bon_mails, frequence_spam_mails) VALUES (%s, %s, %s, %s, %s, %s)")
			data_requete = (lst[0][j], lst[1][j], lst[2][j], lst[3][j], lst[4][j], lst[5][j])
			cursor.execute(requete, data_requete)
		else:
			requete = ("UPDATE mails_annuels SET mails_totaux = %s, bon_mails = %s, spam_mails = %s, frequence_bon_mails = %s, frequence_spam_mails = %s WHERE annee = %s")
			cursor.execute(requete, (lst[1][j], lst[2][j], lst[3][j], lst[4][j], lst[5][j], lst[0][j]))
		j += 1
	conn.commit()

else:
	print("Entrer une valeur valide")

conn.close()