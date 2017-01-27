# This function will check if an interconnection is active by using google.com
# Originally created on July 5th 2016 by Mobin Anandwala
# Based on the following from AlexaPi: https:github.com/novaspirit/AlexaPi/blob/master/main.py

import requests

def Netconnect():
    print('Checking internet connection')
    try:
        r = requests.get('http://www.google.com')
        print('Connection Active')
        return True
    except:
        print('Connection failed')
        print('Please Check Network connection')
        return False

        
