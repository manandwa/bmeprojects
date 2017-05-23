# password generator
# Using the xkcd method of random words a password will be generated and saved into a file
# These passwords will be stored in a text file to be accessed only by the manager

import xkcdpass.xkcd_password as xp

class PasswordGen:

# Attributes of all passwords
    min_length = 5
    max_length = 8

    def __init__(self, name):
        self.name = name

    def wordfilegen(min_length,max_length):
        wordfile = xp.locate_wordfile()
        mywords = xp.generate(wordfile,min_length,max_length)
        return mywords

    def makePass(self):
        mywords = wordfilegen(min_length,max_length)
        password = xp.generate_xkcdpassword(mywords, acrostic="Jarden")
        self.append(password)
