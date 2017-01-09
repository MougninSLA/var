
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