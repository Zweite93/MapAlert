import asyncio
import webbrowser

from config import getConfigs, writeConfig
from dialogs import selectFileDialog, selectDirectoryDialog, showMessage
from mapsfileobserver import MapsFileObserver
from mapsobserver import MapsObserver
from path import mapsFilePath, poeDirectoryIsValid, audioFileIsValid
from sound import playAlert, setAlertSoundPath, stopAlert
from trayicon import TrayIcon

loop = asyncio.get_event_loop()

poeDirectoryPath, alertSoundPath = getConfigs()

setAlertSoundPath(alertSoundPath)

mapsObserver = MapsObserver(poeDirectoryPath)
mapsObserver.readMaps()

mapsFileObserver = MapsFileObserver()
mapsFileObserver.onFileChanged = lambda: mapsObserver.readMaps()


def selectPathOfExileDirectory():
    path = selectDirectoryDialog('Path of Exile')
    if not path:
        return
    if not poeDirectoryIsValid(path):
        showMessage('Invalid directory. Are you sure this is Path of Exile directory?')
        selectPathOfExileDirectory()
        return
    writeConfig('Main', 'PathOfExileDirectoryPath', path)


def openMapsFile():
    webbrowser.open(mapsFilePath)


def selectAlertSound():
    path = selectFileDialog('Alert Sound')
    if not path:
        return
    if not audioFileIsValid(path):
        showMessage('Selected file is not audio file.')
        selectAlertSound()
        return
    setAlertSoundPath(path)
    writeConfig('Audio', 'AlertSoundPath', path)


trayIcon = TrayIcon()
trayIcon.onSelectPathOfExileDirectory = selectPathOfExileDirectory
trayIcon.onSelectAlertSound = selectAlertSound
trayIcon.onOpenMapsFile = openMapsFile
trayIcon.onPlayAlert = playAlert
trayIcon.onStopAlert = stopAlert
trayIcon.onQuit = lambda: loop.call_soon_threadsafe(loop.stop)

try:
    asyncio.ensure_future(mapsObserver.observerCoroutine())
    asyncio.ensure_future(mapsFileObserver.observerCoroutine())
    asyncio.ensure_future(trayIcon.showIcon())
    loop.run_forever()
finally:
    loop.close()
