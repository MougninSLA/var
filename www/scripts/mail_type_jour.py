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

	liste_today_all = {}
	for g in v:
		for key in h.keys():
			if g == key:
				liste_today_all[key] = h[key]
	return liste_today_all

# Fonction qui range et compte les bon mails du jour dans lequel nous sommes dans today_bon_mail
def today_bon_mail():
	os.system("grep 'C=\"250 2.0.0 Ok: queued as' /var/www/scripts/all_mails > /var/www/scripts/good_mail")
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

	liste_today_bon = {}
	for g in v:
		for key in h.keys():
			if g == key:
				liste_today_bon[key] = h[key]
	return liste_today_bon

# Fonction qui range et compte les spams du jour dans lequel nous sommes dans today_spam_mail
def today_spam_mail():
	os.system("sed '/C=\"250 2.0.0 Ok: queued as/d' all_mails > bad_mails")
	os.system("grep \"$(date --rfc-3339=date)\" /var/www/scripts/bad_mails > /var/www/scripts/today_spam_mail")
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

	liste_today_spam = {}
	for g in v:
		for key in h.keys():
			if g == key:	
				liste_today_spam[key] = h[key]
	return liste_today_spam

# Fonction qui range et compte tout les mails dans all_mails
f = open("/var/www/scripts/all_mails")
li = []
for ln in f:
	li.append(ln)
f.close()

def daily_mail():

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

	liste_daily_all = {}
	for g in v:
		for key in h.keys():
			if g == key:
				liste_daily_all[key] = h[key]
	return liste_daily_all

# Fonction qui range et compte les bon mails par jour dans good_mail
def bon_mail():
	os.system("grep 'C=\"250 2.0.0 Ok: queued as' /var/www/scripts/all_mails > /var/www/scripts/good_mail")
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

	liste_daily_bon = {}
	for g in v:
		for key in h.keys():
			if g == key:
				liste_daily_bon[key] = h[key]
	return liste_daily_bon

# Fonction compte les spams par jour dans all_spams

def spam_mail():
	os.system("sed '/C=\"250 2.0.0 Ok: queued as/d' all_mails > bad_mails")
	f = open('/var/www/scripts/bad_mails')
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

	liste_daily_spam = {}
	for g in v:
		for key in h.keys():
			if g == key:
				liste_daily_spam[key] = h[key]
	return liste_daily_spam