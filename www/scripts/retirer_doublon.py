#!/usr/bin/env python3

# On récupère le contenu du fichier good_mail

def del_doublon():
	s = list()
	with open("/var/www/scripts/all_mails", "r") as all_mails:
		# On supprime les doublons du fichier
        	for line in all_mails:
                	if line.strip("\n") and line not in s:
                        	s.append(line)
	        all_mails_str = ''.join(s)	

	with open("/var/www/scripts/all_mails", "w") as all_mails:
        # On écrit la modification
		all_mails.write(all_mails_str)

	v = list()
	with open("/var/www/scripts/all_spams", "r") as all_spams:
		# On supprime les doublons du fichier
		for line in all_spams:
			if line.strip("\n") and line not in v:
				v.append(line)
		all_spams_str = ''.join(v)

	with open("/var/www/scripts/all_spams", "w") as all_spams:
		# On écrit la modification
		all_spams.write(all_spams_str)
