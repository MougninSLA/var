#!/usr/bin/env python3

from mail_type_mois import *
from datetime import date
import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="africainetfier", database="sym")
cursor = conn.cursor()

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

conn.close()