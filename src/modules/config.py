import configparser
from tkinter import messagebox

from dialogs import selectDirectoryDialog
from path import defaultAlertSoundPath, configPath
from pathlib import Path

config = configparser.ConfigParser()


def getConfigs():
    try:
        with open(configPath, 'r', encoding='utf-8') as configFile:
            config.read_file(configFile)
        poeDirectoryPath = config['Main']['PathOfExileDirectoryPath']
        alertSoundPath = config['Audio']['AlertSoundPath']
    except KeyError:
        config['Main'] = {'PathOfExileDirectoryPath': ''}
        config['Audio'] = {'AlertSoundPath': defaultAlertSoundPath}
        with open(configPath, 'w') as configFile:
            config.write(configFile)
        return getConfigs()

    with open(configPath, 'w', encoding='utf-8') as configFile:
        try:
            if not poeDirectoryPath or not Path(poeDirectoryPath).exists():
                poeDirectoryPath = selectDirectoryDialog('Path of Exile')
                if not poeDirectoryPath:
                    messagebox.showinfo('Map Alert', 'Path of Exile directory not selected, application closed.')
                    exit()
                config['Main']['PathOfExileDirectoryPath'] = poeDirectoryPath
            if not alertSoundPath or not Path(alertSoundPath).exists():
                alertSoundPath = defaultAlertSoundPath
                config['Audio']['AlertSoundPath'] = alertSoundPath
        finally:
            config.write(configFile)

    return poeDirectoryPath, alertSoundPath


def writeConfig(category, key, value):
    backup = config[category][key]
    with open(configPath, 'w', encoding='utf-8') as configFile:
        try:
            config[category][key] = value
            config.write(configFile)
        except Exception:
            configFile.seek(0)
            configFile.truncate(0)  # erasing our miserable mistake
            config[category][key] = backup
            config.write(configFile)  # rollback
            raise
