#!/usr/bin/python

# Jacob Mannix [09-03-20]

# Auto Sort Folders

# Specify mainpath to sort through files
mainpath='/Users/jacobmannix/Desktop/folder'
mainfiles = os.listdir(mainpath)

# Folders and filetypes to create and sort
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
    if os.path.isdir(sourcepath + path) == True:
        for file in mainfiles:
            if file.endswith(types):
                shutil.move(os.path.join(sourcepath, file), os.path.join(sourcepath + path, file))
    else:
        os.mkdir(sourcepath + path)