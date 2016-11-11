#!/usr/bin/env python2.7
# coding:utf-8
try:
    import ConfigParser
except:
    import configparser as ConfigParser
conf = ConfigParser.ConfigParser()
conf.read("settings.ini")

db = dict(conf.items("db"))
print(db)
