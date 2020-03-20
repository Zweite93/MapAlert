from pathlib import Path
import asyncio
import PySimpleGUIQt as sg

_iconPath = str(Path.cwd().joinpath('resources', 'icon.ico'))


class TrayIcon:
    _menu = []

    def __init__(self):
        self._trayIcon = sg.SystemTray(['Map Alert',
                                        ['Sound', ['Select Alert Sound', 'Play', 'Stop'],
                                         'Open Maps File',
                                         'Select Path of Exile folder',
                                         'Quit']],
                                       filename=_iconPath)
        self._menuItemsMap = {'Select Alert Sound': lambda: self.onSelectAlertSound(),
                              'Play': lambda: self.onPlayAlert(),
                              'Stop': lambda: self.onStopAlert(),
                              'Open Maps File': lambda: self.onOpenMapsFile(),
                              'Select Path of Exile folder': lambda: self.onSelectPathOfExileDirectory(),
                              'Quit': lambda: self.onQuit()}

    async def showIcon(self):
        while True:
            try:
                menu_item = self._trayIcon.read()
                self._menuItemsMap[menu_item]()
            except (KeyError, RuntimeError):
                # TODO: add logger.
                pass
            await asyncio.sleep(0.1)

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
