#!/usr/bin/env python3

import os
from del_lignes import del_lines, del_lignes_vides
from retirer_doublon import del_doublon, del_doublon_spam

#backup pour les tests
os.system("""cp /var/www/scripts/all_mails /var/www/scripts/all_mails.old
cp /var/www/scripts/all_spams all_spams.old""")

# On récupère les bon mails envoyé ans all_mails
os.system("grep 'C=\"250 2.0.0 Ok: queued as' /var/log/exim4/mainlog >> /var/www/scripts/all_mails")
# On récupère la liste des spams courants dans le dossier
os.system("ls -la --full-time /var/spool/sa-exim/SAteergrube/new > /var/www/scripts/all_spams2")
# On supprime les trois premières lignes du fichiers car elles ne sont pas utiles
del_lines()
# On récupère les spams reçu dans all_spams
os.system("cat /var/www/scripts/all_spams2 >> /var/www/scripts/all_spams")
# On retire les doublons dans le fichier all_spams
del_doublon_spam()
# On ajoute la liste des spams reçu à celle des bon mails dans all_mails
os.system("cat /var/www/scripts/all_spams | cut -d\" \" -f7,10 >> /var/www/scripts/all_mails")
# On supprime les doublons dans le fichier all_mails
del_doublon()
# On retire les lignes vides si il y en a
del_lignes_vides()

#============================================================================

# On compte tous les mails par jour
"""daily_mail()
print("\n")
# On compte tous les mails du mois
monthly_mail()
print("\n")
# On compte tous les mails de l'année
year_mail()
print("\n")
# On compte les mails du jour, où nous sommes
today_mail()
print("\n")
# On compte les bon mails du jour, où nous sommes
today_bon_mail()
print("\n")
# On compte les spams du jour, où nous sommes
today_spam_mail()
print("\n")
# On compte les bon mails de chaque jour
bon_mail()
print("\n")
# On compte les spams de chaque jour
spam_mail()
print("\n")
# On compte les bons mails de chaque mois
bon_mail_mois()
print("\n")
# On compte les spams de chaque mois
spam_mail_mois()
print("\n")
# On compte les bons mails de chaque année
print("\n")
# On compte les spams de chaque année """