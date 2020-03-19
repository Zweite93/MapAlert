import asyncio
import re
import unicodedata

from sound import playAlert
from path import mapsFilePath


class MapsObserver:
    _SYMBOLS = ["#", "@", "%", "&"]
    _maps = []

    def __init__(self, poeFolderPath):
        self._poeFolderPath = poeFolderPath

    async def observerCoroutine(self):
        with open(self._poeFolderPath + '\\logs\\Client.txt', 'r', encoding="utf-8") as logsFile:
            logsFile.seek(0, 2)
            while True:
                where = logsFile.tell()
                line = logsFile.readline()
                if not line:
                    await asyncio.sleep(0.1)
                    logsFile.seek(where)
                else:
                    match = re.search('(?<=You have entered )(.*)(?=.)', line)
                    if match and not any(x in line for x in self._SYMBOLS):
                        enteredMap = match.group(0)
                        if enteredMap in self._maps:
                            playAlert()
                    await asyncio.sleep(0.1)

    def readMaps(self, sysTray=None):
        self._maps.clear()
        with open(mapsFilePath, 'r', encoding="utf-8") as mapsFile:
            for line in mapsFile:
                mapName = self._remove_control_characters(line)
                if not mapName or mapName.startswith('#'):
                    continue
                self._maps.append(mapName)

    def _remove_control_characters(self, string):
        return "".join(ch for ch in string if unicodedata.category(ch)[0] != "C")
