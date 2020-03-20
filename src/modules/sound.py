import pygame
from pygame import mixer

alertSoundPath = ''

mixer.pre_init(44100, -16, 2, 2048)  # fix sound lag
mixer.init()
pygame.init()


def playAlert():
    global alertSoundPath
    mixer.music.load(alertSoundPath)
    mixer.music.play()


def stopAlert():
    mixer.music.stop()


def setAlertSoundPath(path):
    global alertSoundPath
    alertSoundPath = path


def audioFileIsValid(path):
    try:
        mixer.music.load(path)
        return True
    except pygame.error:
        return False
