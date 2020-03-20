import pygame
from pygame import mixer

alertSoundPath = ''

mixer.pre_init(44100, -16, 2, 2048)  # fix sound lag
mixer.init()
pygame.init()


def playAlert(sysTray=None):
    global alertSoundPath
    mixer.music.load(alertSoundPath)
    mixer.music.play()


def setAlertSoundPath(path):
    global alertSoundPath
    alertSoundPath = path
