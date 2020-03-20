import asyncio
import queue

from infi.systray import SysTrayIcon

from path import iconPath


class TrayIcon:
    def __init__(self):
        menuOptions = (('Audio', None, (('Select Alert Sound', None, self._onSelectAlertSound),
                                        ('Play', None, self._onPlayAlert),
                                        ('Stop', None, self._onStopAlert))),
                       ('Open Maps File', None, self._onOpenMapsFile),
                       ('Select Path of Exile folder', None, self._onSelectPathOfExileDirectory))
        self._icon = SysTrayIcon(iconPath, 'Map Alert', menu_options=menuOptions, on_quit=self._onQuit)
        self._callbackQueue = queue.Queue()

    async def show(self):
        self._icon.start()
        while True:
            try:
                callback = self._callbackQueue.get(False)
                callback()
            except queue.Empty:
                await asyncio.sleep(0.1)

    def close(self):
        self._icon.shutdown()

    def onSelectAlertSound(self):
        pass

    def onPlayAlert(self):
        pass

    def onStopAlert(self):
        pass

    def onOpenMapsFile(self):
        pass

    def onSelectPathOfExileDirectory(self):
        pass

    def onQuit(self):
        pass

    def _onSelectAlertSound(self, sysTray):
        self._callbackQueue.put(self.onSelectAlertSound)

    def _onPlayAlert(self, sysTray):
        self._callbackQueue.put(self.onPlayAlert)

    def _onStopAlert(self, sysTray):
        self._callbackQueue.put(self.onStopAlert)

    def _onOpenMapsFile(self, sysTray):
        self._callbackQueue.put(self.onOpenMapsFile)

    def _onSelectPathOfExileDirectory(self, sysTray):
        self._callbackQueue.put(self.onSelectPathOfExileDirectory)

    def _onQuit(self, sysTray):
        self._callbackQueue.put(sysTray.shutdown)
        self._callbackQueue.put(self.onQuit)
