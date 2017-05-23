###############################################################################
#######     TITLE "Project Envirocam Serial Communication Script"      ########
#######     SUBTITLE "COPYRIGHT 2016 BRK BRANDS, INC., FIRST ALERT"    ########
###############################################################################
#######     MODEL:         ENVIROCAM                                   ########
###############################################################################
#######     PROJECT:       ONELINK Enviromental Camera monitor         ########
#######     FILENAME:      serialCom.py                                ########
#######     DATE:          8/8/2016                                   ########
#######     FILE VERSION:  VERSION 1.0                                 ########
#######     SW1 RELEASE:   COMMUNICATION SCRIPTS                       ########
#######     AUTHOR:        MOBIN ANANDWALA                             ########
#######     COMPANY:       BRK BRANDS, INC., FIRST ALERT, INC.         ########
#######                    3901 LIBERTY STREET ROAD                    ########
#######                    AURORA, IL 60504-8122                       ########
###############################################################################
#######     HISTORY:       8/8/2016 FIRST RELEASE                      ########
#######                    8/10/2016 SIMPLIFIED CONFIG FOLDER           #######
#######                    8/17/2016 Added dictionary generating functions ####
#######                    8/18/2016 Added Menu helper functions        #######
#######                    8/19/2016 Added Menu helper functions for all ######
#######                              Added additional CO command         ######
#######                    8/20/2016 Added serial command function for all sensors
#######                    8/22/2016 Added and activated serial command function
#######                             for temperature humidity thermister and
#######                             Activated serial command functions for all sensors
#######                     9/2/2016 Cleaned up code by removing unnecessary functions that are now imported #####
###############################################################################

import serial
import os
import time
import sys
from commandbuild import allsensors, alltemp, allhumid, alltherm, allCO


############################# Configuration ##########################
port = "COM5" #Please Change COM Port Here
baudrate = 9600
######################################################################

delay = 0.5
# #### start serialization #######
ser = serial.Serial(port)
ser.baudrate = baudrate

# Create directories in current workiing directory
config_path = os.getcwd() + '/config'
# Check if config folder is made and if not make it
try:
    os.mkdir(config_path)
except:
    if not os.path.isdir(config_path):
        raise

sensors = allsensors()
temperature = alltemp()
humidity = allhumid()
thermister = alltherm()
co = allCO()

def sensorhelp():
	print('\ta. Read Average')
	print('\ti. Read Instaneous Values')
	print('\tm. Read Current Alarm State')

def temphelp():
    print('\ta. Read Average')
    print('\tc. Read count')
    print('\th. Read or Write high alarm value')
    print('\tl. Read or Write low alarm value')
    print('\td. Read Temperature ID')
    print('\ti. Read Instaneous Value')
    print('\tm. Read Current Alarm state')
    print('\tn. Read number of samples')
    print('\ts. Read temperature sample table')

def humidhelp():
    print('\ta. Read Average')
    print('\tc. Read count')
    print('\th. Read or Write high alarm value')
    print('\tl. Read or Write low alarm value')
    print('\td. Read Humidity ID')
    print('\ti. Read Instaneous Value')
    print('\tm. Read Current Alarm state')
    print('\tn. Read number of samples')
    print('\ts. Read humidity sample table')

def thermhelp():
    print('\ta. Read Average')
    print('\tc. Read count')
    print('\td. Read Thermister ID')
    print('\ti. Read Instaneous Value')
    print('\tn. Read number of samples')
    print('\ts. Read thermister sample table')

def cohelp():
    print('\ta. Read average')
    print('\tb. Read sum')
    print('\tc. Read count')
    print('\td. Read CO ID')
    print('\tg. Read gain')
    print('\ti. Read Instaneous value')
    print('\tk. Read CO Peak')
    print('\tm. Read Current Alarm state')
    print('\tn. Read number of samples')
    print('\tp. Read CO PPM')
    print('\ts. Read CO sample table')
    print('\ty. Read yearly compensated gain')
    print('\tv. Convert PPM to A/D')
    print('\tz. Voltge at 0 PPM')


############################################   Main function Menue #############################################################################################################################
print('\t1. Read all sensors')
print('\t2. Read only temperature')
print('\t3. Read only humidity')
print('\t4. Read only the thermister')
print('\t5. Read only CO')
menu_select = raw_input('Task: ')

########################################### Serial Command Functions bsaed on helper functions ######################################################################

def serialsendcommand(command):
    print('\n')
    ser.write(command + '\r')
    time.sleep(delay)
    while ser.inWaiting() == 0:
        pass
    result = ser.read(ser.inWaiting()).rstrip('\r\n')
    print('\tThe Result is ' + result)

def serialsendwrite(command,value):
    print('\n')
    ser.write(command + '=' + value + '\r')
    time.sleep(delay)
    while ser.inWaiting() == 0:
        pass
    new_value = ser.read(ser.inWaiting()).rstrip('\r\n')
    print('\tThe New Value is ' + new_value)


##def serialallsensors(command):
##    if command == 'a':
##        print('Reading Average of all sensors')
##        serialsendcommand(sensors['sensor average'])
##    elif command == 'i':
##        print('Reading Instaneous value of all sensors')
##        serialsendcommand(sensors['sensor instanteous'])
##    elif command == 'm':
##        print('Reading alarm status of all sensors')
##        serialsendcommand(sensors['sensor alarm'])
##    else:
##        print('invalid command')
##
##def serialtemp(command):
##    if command == 'a':
##        print('Reading temperature average')
##        serialsendcommand(temperature['temp average'])
##    elif command == 'c':
##        print('Reading temperature count')
##        serialsendcommand(temperature['temp activity count'])
##    elif command == 'h':
##        write_yes = raw_input('Are you writing a new value Yes or No? ')
##        if write_yes == 'yes' or write_yes == 'y' or write_yes == 'Yes' or write_yes == 'Y':
##            new_value = raw_input('Please enter the new alarm value: ')
##            print('Writing new high alarm value')
##            serialsendwrite(temperature['temp high'],new_value)
##        if write_yes == 'no' or write_yes == 'n' or write_yes == 'No' or write_yes =='N':
##            print('Reading high alarm value')
##            serialsendcommand(temperature['temp high'])
##    elif command == 'l':
##        write_yes = raw_input('Are you writing a new value Yes or No? ')
##        if write_yes == 'yes' or write_yes == 'y' or write_yes == 'Yes' or write_yes == 'Y':
##            new_value = raw_input('Please enter the new alarm value: ')
##            print('Writing new low alarm value')
##            serialsendwrite(temperature['temp high'],new_value)
##        if write_yes == 'no' or write_yes == 'n' or write_yes == 'No' or write_yes =='N':
##            print('Reading low alarm value')
##            serialsendcommand(temperature['temp low'])
##    elif command == 'd':
##        print('Reading Temperature ID')
##        serialsendcommand(temperature['temp ID'])
##    elif command == 'i':
##        print('Reading instaneous temperature value')
##        serialsendcommand(temperature['temp instanteous'])
##    elif command == 'm':
##        print('Reading current alarm values')
##        serialsendcommand(temperature['temp alarm'])
##    elif command == 'n':
##        print('Reading number of samples')
##        serialsendcommand(temperature['temp number of samples'])
##    elif command == 's':
##        print('Reading sample table')
##        serialsendcommand(temperature['temp samples'])
##    else:
##        print('invalid command')
##
##def serialhumid(command):
##    if command == 'a':
##        print('Reading humidity average')
##        serialsendcommand(humidity['humid average'])
##    elif command == 'c':
##        print('Reading humidity count')
##        serialsendcommand(humidity['humid activity count'])
##    elif command == 'h':
##        write_yes = raw_input('Are you writing a new value Yes or No? ')
##        if write_yes == 'yes' or write_yes == 'y' or write_yes == 'Yes' or write_yes == 'Y':
##            new_value = raw_input('Please enter the new alarm value: ')
##            print('Writing new high alarm value')
##            serialsendwrite(humidity['humid high'],new_value)
##        if write_yes == 'no' or write_yes == 'n' or write_yes == 'No' or write_yes =='N':
##            print('Reading high alarm value')
##            serialsendcommand(humidity['humid high'])
##    elif command == 'l':
##        write_yes = raw_input('Are you writing a new value Yes or No? ')
##        if write_yes == 'yes' or write_yes == 'y' or write_yes == 'Yes' or write_yes == 'Y':
##            new_value = raw_input('Please enter the new alarm value: ')
##            print('Writing new high alarm value')
##            serialsendwrite(humidity['humid low'],new_value)
##        if write_yes == 'no' or write_yes == 'n' or write_yes == 'No' or write_yes =='N':
##            print('Reading low alarm value')
##            serialsendcommand(humidity['humid low'])
##    elif command == 'd':
##        print('Reading Humidity ID')
##        serialsendcommand(humidity['humid ID'])
##    elif command == 'i':
##        print('Reading instaneous humidity value')
##        serialsendcommand(humidity['humid instanteous'])
##    elif command == 'm':
##        print('Reading current alarm values')
##        serialsendcommand(humidity['humid alarm'])
##    elif command == 'n':
##        print('Reading number of samples')
##        serialsendcommand(humidity['humid number of samples'])
##    elif command == 's':
##        print('Reading sample table')
##        serialsendcommand(humidity['humid samples'])
##    else:
##        print('invalid command')
##
##def serialtherm(command):
##    if command == 'a':
##        print('Reading thermister average')
##        serialsendcommand(thermister['therm average'])
##    elif command == 'c':
##        print('Reading thermister count')
##        serialsendcommand(thermister['therm activity counter'])
##    elif command == 'd':
##        print('Reading thermister ID')
##        serialsendcommand(thermister['therm ID'])
##    elif command == 'i':
##        print('Reading instaneous thermister value')
##        serialsendcommand(thermister['therm instanteous'])
##    elif command == 'n':
##        print('Reading number of samples')
##        serialsendcommand(thermister['therm number of samples'])
##    elif command == 's':
##        print('Reading sample table')
##        serialsendcommand(thermister['therm samples'])
##    else:
##        print('invalid command')
##
##def serialCO(command):
##    if command == 'a':
##        print('Reading CO average')
##        serialsendcommand(CO['CO average'])
##    elif command == 'b':
##        print('Reading CO sum')
##        serialsendcommand(CO['COHb Sum'])
##    elif command == 'c':
##        print('Reading CO count')
##        serialsendcommand(CO['CO activity counter'])
##    elif command == 'd':
##        print('Reading CO ID')
##        serialsendcommand(CO['CO ID'])
##    elif command == 'g':
##        print('Reading CO gain')
##        serialsendcommand(CO['CO thermister gain'])
##    elif command == 'i':
##        print('Reading instaneous CO value')
##        serialsendcommand(CO['CO instanteous'])
##    elif command == 'k':
##        print('Reading CO Peak')
##        serialsendcommand(CO['CO peak'])
##    elif command == 'm':
##        print('Reading current alarm values')
##        serialsendcommand(CO['CO alarm'])
##    elif command == 'n':
##        print('Reading number of samples')
##        serialsendcommand(CO['CO number of samples'])
##    elif command == 'p':
##        print('Reading CO PPM value')
##        serialsendcommand(CO['CO Ppm'])
##    elif command == 's':
##        print('Reading sample table')
##        serialsendcommand(CO['CO samples'])
##    elif command == 'y':
##        print('Read yearly compensated CO Gain')
##        serialsendcommand(CO['CO yearly gain'])
##    elif command == 'v':
##        print('Convert PPM to A/D')
##        # serialsendcommand(CO['Convert PP to AD'])
##    elif command == 'z':
##        print('Reading CO voltage at zero offset')
##        serialsendcommand(CO['CO voltage at offset zero'])
##    else:
##        print('invalid command')
##
################################################################### Serial functions ###############################################################################################################
##
##if menu_select == '1':
##	print('Read all sensors')
##	sensorhelp()
##	command_select = raw_input('Plese enter a command listed in the help submenu: ')
##	serialallsensors(command_select)
##elif menu_select == '2':
##	print('Read only temperature')
##	temphelp()
##	command_select = raw_input('Please enter a command listed in the help submenu: ')
##	serialtemp(command_select)
##elif menu_select == '3':
##	print('Read only humidity')
##	humidhelp()
##	command_select = raw_input('Please enter a command listed in the help submenu: ')
##	serialhumid(command_select)
##elif menu_select == '4':
##	print('Read only the thermister')
##	thermhelp()
##	command_select = raw_input('Please enter a command listed in the help submenu: ')
##	serialtherm(command_select)
##elif menu_select == '5':
##	print('Read only CO')
##	cohelp()
##	command_select = raw_input('Please enter a command listed in the help submenu: ')
##	serialCO(command_select)
##else:
##	print('invalid selection')
##	ser.close()
##	sys.exit()
##
