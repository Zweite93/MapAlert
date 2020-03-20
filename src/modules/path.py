import mimetypes
from pathlib import Path

mimetypes.init()

_exeFiles = ['PathOfExileSteam.exe', 'PathOfExile_x64Steam.exe', 'PathOfExile.exe', 'PathOfExile_x64.exe']

defaultAlertSoundPath = Path.cwd().joinpath('resources', 'sound.mp3').as_posix()
configPath = Path.cwd().joinpath('config.ini').as_posix()
mapsFilePath = Path.cwd().joinpath('maps.txt').as_posix()


def poeDirectoryIsValid(path):
    return any(Path(path).joinpath(exe).exists() for exe in _exeFiles)


def audioFileIsValid(path):
    fileType = mimetypes.guess_type(Path(path).suffix)[0]
    return fileType is not None and fileType.split('/')[0] == 'audio'


def getClientLogsPath(poeDirectoryPath):
    return Path(poeDirectoryPath).joinpath('logs', 'Client.txt').as_posix()
