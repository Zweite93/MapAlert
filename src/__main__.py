import asyncio
import webbrowser

from config import getConfigs, writeConfig
from dialogs import selectFileDialog, selectDirectoryDialog
from mapsfileobserver import MapsFileObserver
from mapsobserver import MapsObserver
from sound import playAlert, setVolume, setAlertSoundPath
from trayicon import TrayIcon
from path import mapsFilePath

loop = asyncio.get_event_loop()

poeDirectoryPath, alertSoundPath, alertSoundVolume = getConfigs()

setAlertSoundPath(alertSoundPath)
setVolume(alertSoundVolume)

mapsObserver = MapsObserver(poeDirectoryPath)
mapsObserver.readMaps()

mapsFileObserver = MapsFileObserver()
mapsFileObserver.onFileChanged = lambda: mapsObserver.readMaps()


def selectPathOfExileDirectory(sysTray=None):
    path = selectDirectoryDialog('Path of Exile')
    if not path:
        return
    writeConfig('Main', 'PathOfExileDirectoryPath', path)


def openMapsFile(sysTray=None):
    webbrowser.open(mapsFilePath)


def selectAlertSound(sysTray=None):
    path = selectFileDialog('Alert Sound')
    if not path:
        return
    writeConfig('Audio', 'AlertSoundPath', path)


trayIcon = TrayIcon(lambda sysTray: loop.stop())
trayIcon.addMenuOption('Select Alert Sound', selectAlertSound)
trayIcon.addMenuOption('Play Alert', playAlert)
trayIcon.addMenuOption('Open Maps File', openMapsFile)
trayIcon.addMenuOption('Select Path of Exile folder', selectPathOfExileDirectory)
trayIcon.showIcon()

try:
    asyncio.ensure_future(mapsObserver.observerCoroutine())
    asyncio.ensure_future(mapsFileObserver.observerCoroutine())
    loop.run_forever()
finally:
    loop.close()
