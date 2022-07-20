
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Config file to store Values for the IPC Spot Inspection

"""
import os
import sys
import configparser as ConfigParser


def LoadPreferences(filename):
    configFile = ConfigParser.SafeConfigParser()
    configFile.read(filename)

    if not configFile.sections():
        print (filename+" does not exist - creating file")
        SavePreferences(filename,True)	# Create default values
        return

def SavePreferences(filename, createFile):
    configFile = ConfigParser.SafeConfigParser()
    configFile.read(filename)
    
    configFile["USERINFO"] = {
        "username": "James Bond",
        "loginid": "007",
        "password": "bond007"
    }
    configFile["SERVERCONFIG"] = {
        "host": "http://",
        "port": "8080",
        "ipaddr": "8.8.8.8"
    }
    SaveConfigFile(filename, configFile)

def SaveConfigFile(filename, config):
	with open(filename, 'w+') as configfile:
		config.write(configfile)

	path = os.path.dirname(os.path.abspath(__file__)) + '/' + filename
	os.system('sudo chmod a+w %s' % (path))

#Get the User Information
def get_UserInfo(filename, config):
    config = ConfigParser.SafeConfigParser()
    config.read("config.ini")

    userinfo = config["USERINFO"]
    return userinfo