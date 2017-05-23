###############################################################################
#######     TITLE "FACTORY PASSWORD GENERATION SCRIPT"                 ########
#######     SUBTITLE "COPYRIGHT 2016 BRK BRANDS, INC., FIRST ALERT"    ########
###############################################################################
#######     MODEL:         AC10-500 DC10-500                           ########
###############################################################################
#######     PROJECT:       ONELINK WiFi Smoke and CO Alarm             ########
#######     FILENAME:      config_password_genV4.py                    ########
#######     DATE:          08/4/2016                                   ########
#######     FILE VERSION:  VERSION 4.0                                 ########
#######     AUTHOR:        MOBIN ANANDWALA                             ########
#######     COMPANY:       BRK BRANDS, INC., FIRST ALERT, INC.         ########
#######                    3901 LIBERTY STREET ROAD                    ########
#######                    AURORA, IL 60504-8122                       ########
###############################################################################
#######     HISTORY:       7/12/2016 FIRST RELEASE                     ########
#######                    7/13/2016 ADDED RSA PUBLIC/PRIVATE KEY     #########
#######                    8/4/2016 SAVED PASSWORDS TO ENCRYPTED LIST #########
######                     8/4/2016 REUSED AES ENCRYPTION FUNCTION    #########
######                     8/5/2016 RANDOM GENERATED PASSPHRASE       #########
###############################################################################

import json
from Crypto.Cipher import AES
import random
import base64
import os
from xkcdpass import xkcd_password as xp

# Create password file
current_dir = os.getcwd()
name = current_dir + '/passwords.json'
file = open(name,'wb') # Create file for writing

# Generate password function
def passwordGen():
    wordfile = xp.locate_wordfile()
    mywords = xp.generate_wordlist(wordfile=wordfile, min_length=4,max_length=6) # password length is 4 to 6 words
    password = xp.generate_xkcdpassword(mywords)
    return password

# Encryption function using AES Encryption from generate_config.py
def encryption(privateInfo):
        BLOCK_SIZE = 32
        PADDING = '*'
        pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
        EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
        cipher = AES.new(pad(passphrase))
        encoded = EncodeAES(cipher, privateInfo)
        return encoded

# Generate list of 100 passwords and encrypt them
# Generate random passphrase
passphrase = str(random.randint(100000,999999))
pass_limit = 100
for i in range(pass_limit):
    testpass = passwordGen()
    encryptedPass = encryption(testpass)
    file.write(encryptedPass + '\n')
    file.flush()

# Close file and exit program
file.close()
print('Password database created')
print("Encryption key: " + passphrase)
