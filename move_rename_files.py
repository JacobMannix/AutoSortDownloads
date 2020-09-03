# Jacob Mannix [8-18-20]

# Import Dependencies
from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json

class MyHandler(FileSystemEventHandler):
    i = 0
    def on_modified(self, event):
        new_name = "new_file_" + str(self.i) + ".txt"
        for filename in os.listdir(folder_to_track):
            file_exists = os.path.isfile(folder_destination + "/" + new_name)
            while file_exists:
                self.i += 1
                new_name = "new_file_" + str(self.i) + ".txt"
                file_exists = os.path.isfile(folder_destination + "/" + new_name)
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + new_name
            os.rename(src, new_destination)


folder_to_track = '/Users/jacobmannix/Desktop/Folder1'
folder_destination = '/Users/jacobmannix/Desktop/Folder2'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive = True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
