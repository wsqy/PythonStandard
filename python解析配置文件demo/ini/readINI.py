# coding:utf-8
import ConfigParser


def readConfig(file="sjgame.ini", section=''):
        Config = ConfigParser.ConfigParser()
        Config.read(file)
        config_dict = {}
        for conf in Config.items(section):
                servicename = conf[0]
                servicedir = conf[1]
                config_dict[servicename] = servicedir
        return config_dict

if __name__ == '__main__':
        res = readConfig(file="aa.ini", section='Login_svrlist')
        for k, v in res:
            print(k, "\n", v)
