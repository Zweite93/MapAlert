import distutils.dir_util
import logging
from os import remove
from pathlib import Path


def _getLogFileFolder():
    return Path.cwd().as_posix()


def clearLogFile():
    logFileFolder = _getLogFileFolder()
    logFilePath = Path(logFileFolder).joinpath('logs.txt')
    try:
        remove(logFilePath)
    except OSError:
        pass


class Logger:
    def __init__(self, name):
        self._logger = logging.getLogger(name)
        self._logger.setLevel(logging.INFO)
        if not self._logger.handlers:
            logFileFolder = _getLogFileFolder()
            logs_path = Path(logFileFolder).joinpath('logs.txt')
            distutils.dir_util.mkpath(logFileFolder)
            formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
            log_handler = logging.FileHandler(logs_path)
            log_handler.setFormatter(formatter)
            self._logger.addHandler(log_handler)

    def info(self, msg):
        self._logger.info(msg)

    def warning(self, msg, e=None):
        exc_info = e is not None
        self._logger.warning(msg, exc_info=exc_info)

    def error(self, msg, e=None):
        exc_info = e is not None
        self._logger.error(msg, exc_info=exc_info)

    def critical(self, msg, e=None):
        exc_info = e is not None
        self._logger.critical(msg, exc_info=exc_info)
