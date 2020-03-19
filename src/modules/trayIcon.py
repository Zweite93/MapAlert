from infi.systray import SysTrayIcon

_iconPath = 'resources/icon.ico'


class TrayIcon:
    _trayIcon = None
    _menuOptions = []

    def __init__(self, onQuit):
        self._onQuit = onQuit

    def showIcon(self):
        if self._trayIcon:
            self._trayIcon.shutdown()
        self._trayIcon = SysTrayIcon(_iconPath, 'Map Alert', tuple(self._menuOptions), on_quit=self._onQuit)
        self._trayIcon.start()

    def addMenuOption(self, name, func):
        self._menuOptions.append((name, None, func))
        if self._trayIcon:
            self.showIcon()
