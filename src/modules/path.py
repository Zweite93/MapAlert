from pathlib import Path

defaultAlertSoundPath = str(Path.cwd().joinpath('resources', 'sound.mp3').as_posix())
configPath = str(Path.cwd().joinpath('config.ini').as_posix())
mapsFilePath = str(Path.cwd().joinpath('maps.txt').as_posix())
