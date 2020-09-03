#!/usr/bin/python

# Jacob Mannix [09-03-20]

# Auto Sort Folders

# Import dependencies
import os
import shutil

mainpath = '/Users/jacobmannix/Desktop/folder'
mainfiles = os.listdir(mainpath)

singlefolder = '/media'
if os.path.isdir(mainpath + singlefolder) == False:
    os.mkdir(mainpath + singlefolder)

folders = (
    ( # Images
        "/images",
        ('.jpeg', 'jpg', 'JPG', 'jpeg-2000', 'png', 'HEIC', 'openexr', 'tiff', 'gif', 'raw')
    ),
    ( # Video
        "/videos",
        ('mp4', '.avi', 'mkv', '.h264', '.h265', 'm4v', 'mov', 'mpg', 'mpeg', 'wmv')
    ),
    ( # Audio
        "/audio",
        ('aif', 'cda', 'mid', 'midi', 'mp3', 'mpa', 'ogg', 'wav', 'wma', 'wpl')
    ),
    ( # SVG
        "/images/svg",
        ('.svg')
    )
)

for path, types in folders:
    if os.path.isdir(mainpath + singlefolder + path) == True:
        for file in mainfiles:
            if file.endswith(types):
                shutil.move(os.path.join(mainpath, file), os.path.join(mainpath + singlefolder + path, file))
    else:
        os.mkdir(mainpath + singlefolder + path)
