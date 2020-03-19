import asyncio
import os

from path import mapsFilePath


class MapsFileObserver:
    def __init__(self):
        self._working = False
        self._cachedStamp = 0

    @property
    def working(self):
        return self._working

    def onFileChanged(self):
        pass

    async def observerCoroutine(self):
        while True:
            stamp = os.stat(mapsFilePath).st_mtime
            if stamp != self._cachedStamp:
                self._cachedStamp = stamp
                self.onFileChanged()
            await asyncio.sleep(1)
