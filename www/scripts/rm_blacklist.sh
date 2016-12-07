#!/bin/bash

#---------------------------------------------------------------------
#SYM
#SUPPRESSION D'UNE LIGNE DANS LA BLACKLIST
#AUTEUR MOUGNIN SERGE
#Date 14/11/2016
#---------------------------------------------------------------------

if test -z "$1";
then
        /bin/echo "Erreur ! Entrer en argument l'adresse à supprimer de la blacklist"
else
        #Suppression de la ligne
        /bin/sed "/blacklist_from $1/d" /var/lists/blacklist.cf > /var/lists/temp_blacklist.cf  
        /bin/mv /var/lists/temp_blacklist.cf /var/lists/blacklist.cf        

	#Redemarrage de Spamassassin
        /etc/init.d/spamassassin restart
fi
