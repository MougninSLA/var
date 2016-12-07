#!/bin/bash

#---------------------------------------------------------------------
#SYM
#AJOUT D'UNE LIGNE DANS LA WHITELIST
#AUTEUR MOUGNIN SERGE
#Date 14/11/2016
#---------------------------------------------------------------------

if test -z "$1";
then
        /bin/echo "Erreur ! Entrer en argument l'adresse à blacklister"
else
        #Copie de la ligne
        /bin/echo "whitelist_from@$1" >> /var/lists/whitelist.cf
                
	#Redemarrage de Spamassassin
        /etc/init.d/spamassassin restart
fi
