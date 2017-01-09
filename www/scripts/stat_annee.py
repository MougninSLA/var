#!/usr/bin/env python3

from mail_type_annee import *
from datetime import date
import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="africainetfier", database="sym")
cursor = conn.cursor()

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

conn.close()