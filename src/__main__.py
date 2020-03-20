import asyncio
import webbrowser

from config import getConfigs, writeConfig
from dialogs import selectFileDialog, selectDirectoryDialog, showMessage
from mapsfileobserver import MapsFileObserver
from mapsobserver import MapsObserver
from path import mapsFilePath, poeDirectoryIsValid, audioFileIsValid
from sound import playAlert, setAlertSoundPath
from trayicon import TrayIcon

loop = asyncio.get_event_loop()

poeDirectoryPath, alertSoundPath = getConfigs()

setAlertSoundPath(alertSoundPath)

mapsObserver = MapsObserver(poeDirectoryPath)
mapsObserver.readMaps()

mapsFileObserver = MapsFileObserver()
mapsFileObserver.onFileChanged = lambda: mapsObserver.readMaps()


def selectPathOfExileDirectory(sysTray=None):
    path = selectDirectoryDialog('Path of Exile')
    if not path:
        return
    if not poeDirectoryIsValid(path):
        showMessage('Invalid directory. Are you sure this is Path of Exile directory?')
        selectPathOfExileDirectory()
        return
    writeConfig('Main', 'PathOfExileDirectoryPath', path)


def openMapsFile(sysTray=None):
    webbrowser.open(mapsFilePath)


def selectAlertSound(sysTray=None):
    path = selectFileDialog('Alert Sound')
    if not path:
        return
    if not audioFileIsValid(path):
        showMessage('Selected file is not audio file.')
        selectAlertSound()
        return
    setAlertSoundPath(path)
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
