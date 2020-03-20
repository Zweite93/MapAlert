import os
from path import iconPath
from tkinter import Tk, filedialog, messagebox

root = Tk()
root.withdraw()
root.iconbitmap(iconPath)


def selectDirectoryDialog(directoryName):
    while True:
        path = filedialog.askdirectory(title='Please select a ' + directoryName + ' directory.')
        if not path:
            return None
        if os.path.exists(path):
            return path
        messagebox.showinfo('Map Alert', 'Invalid directory.')


def selectFileDialog(fileName):
    while True:
        path = filedialog.askopenfilename(title='Please select a ' + fileName + ' file.')
        if not path:
            return None
        if os.path.exists(path):
            return path
        messagebox.showinfo('Map Alert', 'Invalid file.')


def showMessage(message):
    messagebox.showinfo('Map Alert', message)
