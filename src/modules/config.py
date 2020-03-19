import configparser
import os
from tkinter import messagebox

from dialogs import selectFileDialog, selectDirectoryDialog

_configPath = 'config.ini'

config = configparser.ConfigParser()
config.read('config.ini')


def getConfigs():
    try:
        poeDirectoryPath = config['Main']['PathOfExileDirectoryPath']
        mapsFilePath = config['Main']['MapsFilePath']
        alertSoundPath = config['Audio']['AlertSoundPath']
        alertSoundVolumeAsString = config['Audio']['Volume']
    except KeyError:
        config['Main'] = {'PathOfExileDirectoryPath': '',
                          'MapsFilePath': 'maps.txt'}
        config['Audio'] = {'AlertSoundPath': 'resources/sound.mp3',
                           'Volume': '0.3'}
        with open(_configPath, 'w') as configFile:
            config.write(configFile)
        return getConfigs()

    with open(_configPath, 'w') as configFile:
        try:
            if not poeDirectoryPath or not os.path.exists(poeDirectoryPath):
                poeDirectoryPath = selectDirectoryDialog('Path of Exile')
                if not poeDirectoryPath:
                    messagebox.showinfo('Map Alert', 'Path of Exile directory not selected, application closed.')
                    exit()
                config['Main']['PathOfExileDirectoryPath'] = poeDirectoryPath
            if not alertSoundPath or not os.path.exists(alertSoundPath):
                alertSoundPath = selectFileDialog('Alert Sound')
                if not alertSoundPath:
                    messagebox.showinfo('Map Alert', 'Alert sound file not selected, application closed.')
                    exit()
                config['Audio']['AlertSoundPath'] = alertSoundPath
            if not mapsFilePath or not os.path.exists(mapsFilePath):
                mapsFilePath = selectFileDialog('Maps')
                if not mapsFilePath:
                    messagebox.showinfo('Map Alert', 'Maps not to run file not selected, application closed.')
                    exit()
                config['Main']['MapsFilePath'] = mapsFilePath
            try:
                alertSoundVolume = float(alertSoundVolumeAsString)
            except ValueError:
                alertSoundVolume = 1.0
                config['Audio']['Volume'] = alertSoundVolume
        finally:
            config.write(configFile)

    return poeDirectoryPath, mapsFilePath, alertSoundPath, alertSoundVolume


def writeConfig(category, key, value):
    with open(_configPath, 'w') as configFile:
        config[category][key] = value
        config.write(configFile)


