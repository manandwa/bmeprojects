# This script will verify the WiFi credentials are active and can connect to a network
# Created by Mobin Anandwala on 11/9/2016

from Checkinternet import Netconnect

ssid = raw_input('Please enter your ssid: ')
password = raw_input('Please enter your password: ')

while True:
    check_cred = raw_input('Are the credentials correct Y/N')
    if check_cred == 'Y':
        break
    elif check_cred == 'N':
        break
    else:
        pass

# Check connectiong
while Netconnect() == True:
    print('Valid credentials')
    break
    if Netconnect() == False:
        print('Invalid Credentials!')
