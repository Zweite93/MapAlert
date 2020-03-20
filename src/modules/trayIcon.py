import asyncio
from pathlib import Path

import PySimpleGUIQt as sg

_iconPath = str(Path.cwd().joinpath('resources', 'icon.ico'))


class TrayIcon:
    _menuItems = {}
    _menu = []

    def __init__(self):
        self._trayIcon = sg.SystemTray("Map Alert", filename=_iconPath)
        self._menu.append('1')
        self._menu.append([])

    async def showIcon(self):
        while True:
            menu_item = self._trayIcon.read()
            if menu_item in self._menuItems:
                self._menuItems[menu_item]()
            await asyncio.sleep(0.1)

    def addMenuOption(self, name, func):
        self._menuItems[name] = func
        self._menu[1].append(name)
        self._trayIcon.Update(menu=self._menu)
