import asyncio
import os


class MapsFileObserver:
    def __init__(self, mapsFilePath):
        self._mapsFilePath = mapsFilePath
        self._working = False
        self._cachedStamp = 0

    @property
    def working(self):
        return self._working

    def onFileChanged(self):
        pass

    async def observerCoroutine(self):
        while True:
            stamp = os.stat(self._mapsFilePath).st_mtime
            if stamp != self._cachedStamp:
                self._cachedStamp = stamp
                self.onFileChanged()
            await asyncio.sleep(1)
