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
signup_form["u"]