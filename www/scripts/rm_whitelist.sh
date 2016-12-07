#!/bin/bash

#---------------------------------------------------------------------
#SYM
#SUPPRESSION D'UNE LIGNE DANS LA WHITELIST
#AUTEUR MOUGNIN SERGE
#Date 14/11/2016
#---------------------------------------------------------------------

if test -z "$1";
then
        /bin/echo "Erreur ! Entrer en argument l'adresse à enlever de la WhiteList"
else
        #Suppression de la ligne
        /bin/sed "/whitelist_from@$1/d" /var/lists/whitelist.cf > /var/lists/temp_whitelist.cf  
        /bin/mv /var/lists/temp_whitelist.cf /var/lists/whitelist.cf        

	#Redemarrage de Spamassassin
        /etc/init.d/spamassassin restart
fi
