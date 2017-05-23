# Mobin Anandwala
# 08/03/2016
# This code will generate a random list of codes for two factor authentication
# this code was based on the following: https://www.twilio.com/docs/tutorials/walkthrough/sms-two-factor-authentication/python/flask

import random

def codegen():
    test = str(random.randrange(100000,999999))
    return test
