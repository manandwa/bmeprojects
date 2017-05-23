# password generator
# Using the xkcd method of random words a password will be generated and saved into a file
# These passwords will be stored in a text file to be accessed only by the manager
# This is created as a class and will be used inside of the configuration manager
# Example taken from learning python with raspberry pi

import xkcdpass.xkcd_password as xp

class PasswordGen():
    # core attributes
    min_words = 5
    max_words = 8

    # what do you want to happen when this class is called
    def __init__(self,name):
        self.name = name # create an empty list

    def makePass():
        wordfile = xp.locate_wordfile()
        mywords = xp.generate_wordlist(wordfile, min_length,max_length)
        password = xp.generate_xkcdpassword(mywords, acrostic="Jarden")
        self.password.append(password)
