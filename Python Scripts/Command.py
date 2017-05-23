# Mobin Anandwala
# 08/29/2016
# This file is to test a theory to generate a dictionary using a self contained class instead of separate functions


class Command(object):
    def __init__(self,description,command):
        self.description = description
        self.command = command

    def kvgen(self,description,command):
        self.command_key_value = (description,command)
        return self.command_key_value

    def listgen(self,description,command):
        self.commandlist = [self.kvgen(description,command)]
        return self.commandlist

    def addlist(self,commandlist,description,command):
        self.commandlist.append(self.kvgen(description,command))
        return self.commandlist

    def dictgen(self,commandlist):
        self.command_dict = dict(self.commandlist)
        return self.command_dict

    
