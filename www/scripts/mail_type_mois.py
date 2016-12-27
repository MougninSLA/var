#!/usr/bin/env python3

import os

f = open('/var/www/scripts/all_mails')
li = []
for ln in f:
        li.append(ln)
f.close()

def monthly_mail():

        lim = []
        for i in li:
                i = i.split()
                y = i[0].split("-")
                del(y[2])
                y = "-".join(y)
                lim.append(y)

        s = {}
        while lim:
                a = lim.count(lim[0])
                s[lim[0]] = a
                i = lim[0]
                lim = [y for y in lim if y != i]
        v = sorted(s)

        liste_monthly_all = {}
        for g in v:
                for key in s.keys():
                        if g == key:
                                liste_monthly_all[key] = s[key]
        return liste_monthly_all

# Fonction qui range et compte les bon mails par mois dans good_mail
def bon_mail_mois():
        os.system("grep 'C=\"250 2.0.0 Ok: queued as' /var/www/scripts/all_mails > /var/www/scripts/good_mail")
        f = open('/var/www/scripts/good_mail')
        li = []
        for ln in f:
                li.append(ln)
        f.close()
        lim = []
        for i in li:
                i = i.split()
                y = i[0].split("-")
                del(y[2])
                y = "-".join(y)
                lim.append(y)

        s = {}
        while lim:
                a = lim.count(lim[0])
                s[lim[0]] = a
                i = lim[0]
                lim = [y for y in lim if y != i]
        v = sorted(s)

        liste_monthly_bon = {}
        for g in v:
                for key in s.keys():
                        if g == key:
                                liste_monthly_bon[key] = s[key]
        return liste_monthly_bon

# Fonction compte les spams par mois dans all_spams

def spam_mail_mois():
        f = open('/var/www/scripts/all_spams')
        li = []
        for ln in f:
                li.append(ln)
        f.close()
        lim = []
        for i in li:
                i = i.split()
                y = i[0].split("-")
                del(y[2])
                y = "-".join(y)
                lim.append(y)

        s = {}
        while lim:
                a = lim.count(lim[0])
                s[lim[0]] = a
                i = lim[0]
                lim = [y for y in lim if y != i]
        v = sorted(s)

        liste_monthly_spam = {}
        for g in v:
                for key in s.keys():
                        if g == key:
                                liste_monthly_spam[key] = s[key]
        return liste_monthly_spam