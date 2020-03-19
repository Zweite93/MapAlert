import sys

import setuptools
from cx_Freeze import setup, Executable

shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     "Map Alert",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]MapAlert.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     'TARGETDIR'  # WkDir
     )
]

msi_data = {'Shortcut': shortcut_table}
bdist_msi_options = {'data': msi_data}

build_exe_options = {'path': sys.path + ['modules'],
                     'packages': setuptools.find_packages(),
                     'include_files': ['maps.txt',
                                       ('resources/sound.mp3', 'resources/sound.mp3'),
                                       ('resources/icon.ico', 'resources/icon.ico')],
                     'includes': ['modules/__init__', 'modules/config', 'modules/dialogs', 'modules/mapsfileobserver',
                                  'modules/mapsobserver', 'modules/sound', 'modules/trayicon']}

with open('../README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='Map Alert',
    version='1.0',
    author='Zweite93',
    description='Plays an alert sound when you entering wrong map.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Zweite93/MapAlert',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Windows',
    ],
    python_requires='>=3.7',
    executables=[Executable('__main__.py', shortcutName='Map Alert',
                            shortcutDir='DesktopFolder', icon='resources/icon.ico',
                            targetName='MapAlert', base='Win32GUI')],
    options={'build_exe': build_exe_options, 'bdist_msi': bdist_msi_options},
    install_requires=['Pillow', 'infi.systray'])
