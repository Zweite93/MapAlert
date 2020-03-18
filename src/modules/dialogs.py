import os
from tkinter import Tk, filedialog, messagebox


def selectDirectoryDialog(directoryName):
    root = Tk()
    root.withdraw()
    while True:
        path = filedialog.askdirectory(title='Please select a ' + directoryName + ' directory.')
        if not path:
            return None
        if not os.path.exists(path):
            messagebox.showinfo('Map Alert', 'Invalid directory.')
            continue
        return path


def selectFileDialog(fileName):
    root = Tk()
    root.withdraw()
    while True:
        path = filedialog.askopenfilename(title='Please select a ' + fileName + ' file.')
        if not path:
            return None
        if not os.path.exists(path):
            messagebox.showinfo('Atlas Alert', 'Invalid file.')
            continue
        return path
