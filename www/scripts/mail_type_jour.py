#!/usr/bin/env python3

import os

# Fonction qui range et compte les mails d'aujourd'hui dans today_mail
def today_mail():
	os.system("grep \"$(date --rfc-3339=date)\" /var/www/scripts/all_mails > /var/www/scripts/today_mail")
	f = open('/var/www/scripts/today_mail')
	li = []
	for ln in f:
		li.append(ln)
	f.close()
	li2 = []
	for i in li:
		i = i.split()
		li2.append(i[0])
	h = {}
	while li2:
		a = li2.count(li2[0])
		h[li2[0]] = a
		i = li2[0]
		li2 = [y for y in li2 if y != i]
	v = sorted(h)

	print("Les mails totaux reçus aujourd'hui")
	for g in v:
		for key in h.keys():
			if g == key:
				print("Le ",key,", il y a eu ",h[key]," mail(s)")

# Fonction qui range et compte les bon mails du jour dans lequel nous sommes dans today_bon_mail
def today_bon_mail():
	os.system("grep \"C=\"250 2.0.0 Ok: queued as\" /var/www/scripts/all_mails > /var/www/scripts/good_mail")
	os.system("grep \"$(date --rfc-3339=date)\" /var/www/scripts/good_mail > /var/www/scripts/today_bon_mail")
	f = open('/var/www/scripts/today_bon_mail')
	li = []
	for ln in f:
		li.append(ln)
	f.close()
	li2 = []
	for i in li:
		i = i.split()
		li2.append(i[0])
	h = {}
	while li2:
		a = li2.count(li2[0])
		h[li2[0]] = a
		i = li2[0]
		li2 = [y for y in li2 if y != i]
	v = sorted(h)

	print("Les mails valides totaux reçus chaque aujourd'hui")
	for g in v:
		for key in h.keys():
			if g == key:
				print("Le ",key,", il y a eu ",h[key]," bon mail(s)")

# Fonction qui range et compte les spams du jour dans lequel nous sommes dans today_spam_mail
def today_spam_mail():
	os.system("grep \"$(date --rfc-3339=date)\" /var/www/scripts/all_spams | cut -d\" \" -f7,10 > /var/www/scripts/today_spam_mail")
	f = open('/var/www/scripts/today_spam_mail')
	li = []
	for ln in f:
		li.append(ln)
	f.close()
	li2 = []
	for i in li:
		i = i.split()
		li2.append(i[0])
	h = {}
	while li2:
		a = li2.count(li2[0])
		h[li2[0]] = a
		i = li2[0]
		li2 = [y for y in li2 if y != i]
	v = sorted(h)

	print("Les spams totaux reçus aujourd'hui")
	for g in v:
		for key in h.keys():
			if g == key:
				print("Le ",key,", il y a eu ",h[key]," spam(s)")	

# Fonction qui range et compte les bon mails par jour dans good_mail
def bon_mail():
	os.system("grep \"C=\"250 2.0.0 Ok: queued as\" /var/www/scripts/all_mails > /var/www/scripts/good_mail")
	f = open('/var/www/scripts/good_mail')
	li = []
	for ln in f:
		li.append(ln)
	f.close()
	li2 = []
	for i in li:
		i = i.split()
		li2.append(i[0])
	h = {}
	while li2:
		a = li2.count(li2[0])
		h[li2[0]] = a
		i = li2[0]
		li2 = [y for y in li2 if y != i]
	v = sorted(h)

	print("Les mails valident totaux reçus chaque jour")
	for g in v:
		for key in h.keys():
			if g == key:
				print("Le ",key,", il y a eu ",h[key]," bon mail(s)")

# Fonction compte les spams par jour dans all_spams

def spam_mail():
	f = open('/var/www/scripts/all_spams')
	li = []
	for ln in f:
		li.append(ln)
	f.close()
	li2 = []
	for i in li:
		i = i.split()
		li2.append(i[5])
	h = {}
	while li2:
		a = li2.count(li2[0])
		h[li2[0]] = a
		i = li2[0]
		li2 = [y for y in li2 if y != i]
	v = sorted(h)

	print("Les spams totaux reçus chaque jour")
	for g in v:
		for key in h.keys():
			if g == key:
				print("Le ",key,", il y a eu ",h[key]," spam(s)")
