# Mobin Anandawla
# 07/21/2016
# Quick test for xkcd password generation

import xkcdpass.xkcd_password as xp

wordfile = xp.locate_wordfile()
mywords = xp.generate_wordlist(wordfile=wordfile,min_length=5,max_length=8)
password = xp.generate_xkcdpassword(mywords, acrostic="Jarden")
print(password)
