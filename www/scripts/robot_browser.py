#!/usr/bin/env python3

import re
from robobrowser import RoboBrowser

"""
# Navigation sur Genius(c'est un site de lyric) PS: c'est un site pour tester
browser = RoboBrowser(history=True)
browser.open("http://genius.com/")

# Recherche du groupe de chanteurs the cranberries
form = browser.get_form(action="/search")
form 		# <RoboForm singer=>
form["singer"].value = "the cranberries"
browser.submit_form(form)

# Récupération de la première musique
songs = browser.select(".song_link")
browser.follow_link(songs[0])
lyrics = browser.select(".lyrics")
lyrics[0].text

# Retour à la page de des résultats de mes recherches
browser.back()

# Récupération de ma chanson favorite
song_link = browser.get_link("zombie")
browser.follow_link(song_link)

"""

browser = RoboBrowser()
browser.open("https://www.celio.com/register")

# ON sera dirigé sur la page d'inscription de celio
# Et on récupère le formulaire
signup_form = browser.get_form(class_="register")

# Vérification des valeurs
signup_form["user[titleCode]"].value = "mr"
signup_form["user[lastName]"].value = "Sym"
signup_form["user[firstName]"].value = "Secure Your Mail"
signup_form["user[birthdayDay]"].value = "21"
signup_form["user[birthdayMonth]"].value = "03"
signup_form["user[birthdayYear]"].value = "1989"
signup_form["user[mobilephoneCode]"].value = "612345678"
signup_form["user[defaultAdressline1]"].value = "08 rue secureyourmail"
signup_form["user[defaultAdress.postalCode]"].value = "85123"
signup_form["user[defaultAddress.town]"].value = "fraise"
signup_form["user[defaultAdress.country.isocode]"].value = "FR"
signup_form["user[email]"].value = "sym@sym.itinet.fr"
signup_form["user[emailConfirmation]"].value = "sym@sym.itinet.fr"
signup_form["user[password]"].value = "secureyourmail123"
signup_form["user[passwordConfirmation]"].value = "secureyourmail123"

# On soumet le formulaire
browser.submit_form(signup_form)