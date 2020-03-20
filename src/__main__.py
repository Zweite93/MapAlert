import asyncio
import webbrowser
from concurrent.futures import CancelledError

from config import getConfigs, writeConfig
from dialogs import selectFileDialog, selectDirectoryDialog, showMessage
from logger import Logger, clearLogFile
from mapsfileobserver import MapsFileObserver
from mapsobserver import MapsObserver
from path import mapsFilePath, poeDirectoryIsValid
from sound import playAlert, setAlertSoundPath, stopAlert, audioFileIsValid
from trayicon import TrayIcon

clearLogFile()
logger = Logger('main')
mainLoop = asyncio.get_event_loop()
trayIcon = TrayIcon()


def _selectPathOfExileDirectory():
    path = selectDirectoryDialog('Path of Exile')
    if not path:
        return
    if not poeDirectoryIsValid(path):
        showMessage('Invalid directory. Are you sure this is Path of Exile directory?')
        _selectPathOfExileDirectory()
        return
    writeConfig('Main', 'PathOfExileDirectoryPath', path)


def _openMapsFile():
    webbrowser.open(mapsFilePath)


def _selectAlertSound():
    path = selectFileDialog('Alert Sound')
    if not path:
        return
    if not audioFileIsValid(path):
        showMessage('Selected file is not audio file.')
        _selectAlertSound()
        return
    setAlertSoundPath(path)
    writeConfig('Audio', 'AlertSoundPath', path)


async def main():
    poeDirectoryPath, alertSoundPath = getConfigs()
    setAlertSoundPath(alertSoundPath)

    mapsObserver = MapsObserver(poeDirectoryPath)
    mapsObserver.readMaps()
    mapObserverTask = asyncio.ensure_future(mapsObserver.observerCoroutine())

    mapsFileObserver = MapsFileObserver()
    mapsFileObserver.onFileChanged = lambda: mapsObserver.readMaps()
    mapFileObserverTask = asyncio.ensure_future(mapsFileObserver.observerCoroutine())

    trayIcon.onSelectPathOfExileDirectory = _selectPathOfExileDirectory
    trayIcon.onSelectAlertSound = _selectAlertSound
    trayIcon.onOpenMapsFile = _openMapsFile
    trayIcon.onPlayAlert = playAlert
    trayIcon.onStopAlert = stopAlert

    def onStop():
        mapObserverTask.cancel()
        mapFileObserverTask.cancel()
        iconTask.cancel()

    trayIcon.onQuit = onStop
    iconTask = asyncio.ensure_future(trayIcon.show())

    await mapObserverTask
    await mapFileObserverTask
    await iconTask


try:
    mainLoop.run_until_complete(main())
except CancelledError:
    logger.info('Task cancelled.')
except Exception as e:
    logger.critical('Unhandled Exception in main loop.', e)
    raise
finally:
    mainLoop.close()
