from configparser import ConfigParser


def getConfigData(section, key):
    config = ConfigParser()
    config.read("..\\ConfigurationData\\config.ini")
    return config.get(section, key)


def getTestData(section, key):
    config = ConfigParser()
    config.read("..\\ConfigurationData\\testDaya.ini")
    return config.get(section, key)
