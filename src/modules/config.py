import configparser
import os
from tkinter import messagebox

from dialogs import selectDirectoryDialog
from path import defaultAlertSoundPath, configPath

config = configparser.ConfigParser()
config.read(configPath)


def getConfigs():
    try:
        poeDirectoryPath = config['Main']['PathOfExileDirectoryPath']
        alertSoundPath = config['Audio']['AlertSoundPath']
        alertSoundVolumeAsString = config['Audio']['Volume']
    except KeyError:
        config['Main'] = {'PathOfExileDirectoryPath': ''}
        config['Audio'] = {'AlertSoundPath': defaultAlertSoundPath, 'Volume': '0.3'}
        with open(configPath, 'w') as configFile:
            config.write(configFile)
        return getConfigs()

    with open(configPath, 'w') as configFile:
        try:
            if not poeDirectoryPath or not os.path.exists(poeDirectoryPath):
                poeDirectoryPath = selectDirectoryDialog('Path of Exile')
                if not poeDirectoryPath:
                    messagebox.showinfo('Map Alert', 'Path of Exile directory not selected, application closed.')
                    exit()
                config['Main']['PathOfExileDirectoryPath'] = poeDirectoryPath
            if not alertSoundPath or not os.path.exists(alertSoundPath):
                alertSoundPath = defaultAlertSoundPath
                config['Audio']['AlertSoundPath'] = alertSoundPath
            try:
                alertSoundVolume = float(alertSoundVolumeAsString)
            except ValueError:
                alertSoundVolume = 1.0
                config['Audio']['Volume'] = alertSoundVolume
        finally:
            config.write(configFile)

    return poeDirectoryPath, alertSoundPath, alertSoundVolume


def writeConfig(category, key, value):
    with open(configPath, 'w') as configFile:
        config[category][key] = value
        config.write(configFile)
