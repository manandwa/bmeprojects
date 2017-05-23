# Mobin Anandwala
# 08/31/2016
# This code will build the dictionaries holding the sensor core commands

from Command import Command

# All sensors function
def allsensors():
    sensors = Command('sensor average','sa')
    sensors.sensorlist = sensors.listgen(sensors.description,sensors.command)
    sensors.sensorlist = sensors.addlist(sensors.sensorlist,'sensor instanteous','si')
    sensors.sensorlist = sensors.addlist(sensors.sensorlist,'sensor alarm','sm')
    sensors.sensordict = sensors.dictgen(sensors.sensorlist)
    return sensors.sensordict


# All temperature function
def alltemp():
    temperature = Command('temperature average','ta')
    temperature.templist = temperature.listgen(temperature.description,temperature.command)
    temperature.templist = temperature.addlist(temperature.templist,'temperature Activity Count','tc')
    temperature.templist = temperature.addlist(temperature.templist,'temperature ID','td')
    temperature.templist = temperature.addlist(temperature.templist,'temperature high','th')
    temperature.templist = temperature.addlist(temperature.templist,'temperature instanteous','ti')
    temperature.templist = temperature.addlist(temperature.templist,'temperature low','tl')
    temperature.templist = temperature.addlist(temperature.templist,'temperature alarm','tm')
    temperature.templist = temperature.addlist(temperature.templist,'temperature number of samples','tn')
    temperature.templist = temperature.addlist(temperature.templist,'temperature samples','ts')
    temperature.tempdict = temperature.dictgen(temperature.templist)
    return temperature.tempdict


def allhumid():
    humidity = Command('humidity average','ha')
    humidity.humidlist = humidity.listgen(humidity.description,humidity.command)
    humidity.humidlist = humidity.addlist(humidity.humidlist,'humidity Activity Count','hc')
    humidity.humidlist = humidity.addlist(humidity.humidlist,'humidity ID','hd')
    humidity.humidlist = humidity.addlist(humidity.humidlist,'humidity high','hh')
    humidity.humidlist = humidity.addlist(humidity.humidlist,'humidity instanteous','hi')
    humidity.humidlist = humidity.addlist(humidity.humidlist,'humidity low','hl')
    humidity.humidlist = humidity.addlist(humidity.humidlist,'humidity number of samples','hn')
    humidity.humidlist = humidity.addlist(humidity.humidlist,'humidity samples','hs')
    humidity.humiddict = humidity.dictgen(humidity.humidlist)
    return humidity.humiddict

def alltherm():
    thermister = Command('thermister average','ra')
    thermister.thermlist = thermister.listgen(thermister.description,thermister.command)
    thermister.thermlist = thermister.addlist(thermister.thermlist,'thermister Activity counter','rc')
    thermister.thermlist = thermister.addlist(thermister.thermlist,'thermister ID','rd')
    thermister.thermlist = thermister.addlist(thermister.thermlist,'thermister instanteous','ri')
    thermister.thermlist = thermister.addlist(thermister.thermlist,'thermister number of samples','rn')
    thermister.thermlist = thermister.addlist(thermister.thermlist,'thermister samples','rs')
    thermister.thermdict = thermister.dictgen(thermister.thermlist)
    return thermister.thermdict

def allCO():
    co = Command('CO average','ca')
    co.colist = co.listgen(co.description,co.command)
    co.colist = co.addlist(co.colist,'CO Activity counter','cc')
    co.colist = co.addlist(co.colist,'CO ID','cd')
    co.colist = co.addlist(co.colist,'CO thermister','cg')
    co.colist = co.addlist(co.colist,'CO instanteous','ci')
    co.colist = co.addlist(co.colist,'CO Peak','ck')
    co.colist = co.addlist(co.colist,'CO alarm','cm')
    co.colist = co.addlist(co.colist,'CO number of samples','cn')
    co.colist = co.addlist(co.colist,'CO PPM','cp')
    co.colist = co.addlist(co.colist,'CO samples','cs')
    co.colist = co.addlist(co.colist,'CO yearly gain','cy')
    co.colist = co.addlist(co.colist,'CO voltage at offset zero','cz')
    co.colist = co.addlist(co.colist,'CO Hb sum','cb')
    co.colist = co.addlist(co.colist,'CO Convert PP to AD','cv')
    co.codict = co.dictgen(co.colist)
    return co.codict

    
    
    
    
