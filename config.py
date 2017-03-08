# -*- coding: gbk -*-
import ConfigParser,re

cf = ConfigParser.ConfigParser()
configFile = 'config.ini'



def getTemp(option):
    data = ''
    try:
        cf.read(configFile)
        data = cf.get('TEMP', option)
        data = unicode(data,'gbk')
    except:
        data = ''
    return data

def saveTemp(option,value):
    cf.read(configFile)
    section = 'TEMP'
    try:
        cf.set(section, option,unicode(value).encode('gbk'))
        cf.write(open(configFile,'w')) 
    except Exception,e:
        print e

def getConfig(option):
    data = ''
    try:
        cf.read(configFile)
        data = cf.get('CONFIG', option)
        data = unicode(data,'gbk')
    except:
        data = ''
    return data    

