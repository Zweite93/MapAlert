import re
import threading
import time

import unicodedata
from sound import playAlert


class MapsObserver:
    _SYMBOLS = ["#", "@", "%", "&"]
    _maps = []

    working = False

    def __init__(self, poeFolderPath):
        self._poeFolderPath = poeFolderPath

    def start(self):
        self.working = True
        t = threading.Thread(target=self._doWork, args=())
        t.start()

    def stop(self):
        self.working = False

    def _doWork(self):
        with open(self._poeFolderPath + '\\logs\\Client.txt', 'r', encoding="utf-8") as logsFile:
            logsFile.seek(0, 2)
            while self.working:
                where = logsFile.tell()
                line = logsFile.readline()
                if not line:
                    time.sleep(1)
                    logsFile.seek(where)
                else:
                    match = re.search('(?<=You have entered )(.*)(?=.)', line)
                    if match and not any(x in line for x in self._SYMBOLS):
                        enteredMap = match.group(0)
                        if enteredMap in self._maps:
                            playAlert()

    def readMaps(self, path, sysTray=None):
        self._maps.clear()
        with open(path, 'r', encoding="utf-8") as mapsFile:
            for line in mapsFile:
                mapName = self._remove_control_characters(line)
                if not mapName or mapName.startswith('#'):
                    continue
                self._maps.append(mapName)

    def _remove_control_characters(self, string):
        return "".join(ch for ch in string if unicodedata.category(ch)[0] != "C")
