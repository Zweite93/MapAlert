from infi.systray import SysTrayIcon

_tryIcon = None
menuOptions = []


def showIcon(iconPath, onQuit):     # this will block thread until icon is stopped
    global _tryIcon
    _tryIcon = SysTrayIcon(iconPath, 'Map Alert', tuple(menuOptions), on_quit=onQuit)
    _tryIcon.start()


def addMenuOption(name, func):
    if _tryIcon:
        raise NotImplemented()
    menuOptions.append((name, None, func))
