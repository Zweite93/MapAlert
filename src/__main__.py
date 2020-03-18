from mapsobserver import MapsObserver
from trayIcon import showIcon, addMenuOption
from sound import playAlert, setVolume, setAlertSoundPath
from config import getConfigs, writeConfig
from dialogs import selectFileDialog, selectDirectoryDialog

_iconPath = 'resources/icon.ico'

poeDirectoryPath, mapsFilePath, alertSoundPath, alertSoundVolume = getConfigs()

setAlertSoundPath(alertSoundPath)
setVolume(alertSoundVolume)

mapsObserver = MapsObserver(poeDirectoryPath)
mapsObserver.readMaps(mapsFilePath)
mapsObserver.start()


def selectPathOfExileDirectory(sysTray=None):
    path = selectDirectoryDialog('Path of Exile')
    if not path:
        return
    writeConfig('Main', 'PathOfExileDirectoryPath', path)


def selectMapsFile(sysTray=None):
    path = selectFileDialog('Maps')
    if not path:
        return
    writeConfig('Main', 'MapsFilePath', path)


def selectAlertSound(sysTray=None):
    path = selectFileDialog('Alert Sound')
    if not path:
        return
    writeConfig('Audio', 'AlertSoundPath', path)


def onQuit(sysTray):
    mapsObserver.stop()
    exit()


addMenuOption('Select alert sound', selectAlertSound)
addMenuOption('Play Alert', playAlert)
addMenuOption('Select maps file', selectMapsFile)
addMenuOption('Reload Maps', lambda: mapsObserver.readMaps(mapsFilePath))
addMenuOption('Select Path of Exile folder', selectPathOfExileDirectory)
showIcon(_iconPath, onQuit)
