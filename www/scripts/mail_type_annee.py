#!/usr/bin/env python3

import os

f = open('/var/www/scripts/all_mails')
li = []
for ln in f:
        li.append(ln)
f.close()

def year_mail():

        lia = []
        for i in li:
                i = i.split()
                y = i[0].split("-")
                del(y[-2:])
                y = "".join(y)
                lia.append(y)
        z = {}
        while lia:
                a = lia.count(lia[0])
                z[lia[0]] = a
                i = lia[0]
                lia = [y for y in lia if y != i]
        v = sorted(z)

        liste_year_all = {}
        for g in v:
                for key in z.keys():
                        if g == key:
                                liste_year_all[key] = z[key]
        return liste_year_all

# Fonction qui range et compte les bon mails par année dans good_mail
def bon_mail_annee():
        os.system("grep 'C=\"250 2.0.0 Ok: queued as' /var/www/scripts/all_mails > /var/www/scripts/good_mail")
        f = open('/var/www/scripts/good_mail')
        li = []
        for ln in f:
                li.append(ln)
        f.close()
        lia = []
        for i in li:
                i = i.split()
                y = i[0].split("-")
                del(y[-2:])
                y = "".join(y)
                lia.append(y)

        z = {}
        while lia:
                a = lia.count(lia[0])
                z[lia[0]] = a
                i = lia[0]
                lia = [y for y in lia if y != i]
        v = sorted(z)
        
        liste_year_bon = {}
        for g in v:
                for key in z.keys():
                        if g == key:
                                liste_year_bon[key] = z[key]
        return liste_year_bon

# Fonction qui compte les spams par année dans all_spams
def spam_mail_annee():
        os.system("sed '/C=\"250 2.0.0 Ok: queued as/d' all_mails > bad_mails")
        f = open('/var/www/scripts/bad_mails')
        li = []
        for ln in f:
                li.append(ln)
        f.close()
        lia = []
        for i in li:
                i = i.split()
                y = i[0].split("-")
                del(y[-2:])
                y = "".join(y)
                lia.append(y)

        z = {}
        while lia:
                a = lia.count(lia[0])
                z[lia[0]] = a
                i = lia[0]
                lia = [y for y in lia if y != i]
        v = sorted(z)

        liste_year_spam = {}
        for g in v:
                for key in z.keys():
                        if g == key:
                                liste_year_spam[key] = z[key]
        return liste_year_spam