import setuptools
from cx_Freeze import setup, Executable

build_exe_options = {"packages": setuptools.find_packages(),
                     "include_files": ['config.ini', 'maps.txt',
                                       'resources/sound.mp3', 'resources/icon.ico']}

with open('../README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name="Map Alert",
    version="1.0",
    author="Zweite93",
    description="Plays an alert sound when you entering wrong map.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zweite93/MapAlert",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
    python_requires='>=3.7',
    executables=[Executable('__main__.py', shortcutName="Atlas Alert",
                            shortcutDir="DesktopFolder", icon='resources/icon.ico')],
    options={"build_exe": build_exe_options},
    install_requires=['Pillow', 'infi.systray'])
