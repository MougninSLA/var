#!/usr/bin/env python3

from mail_type_jour import *
from datetime import date
import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="africainetfier", database="test1")
cursor = conn.cursor()

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

conn.close()