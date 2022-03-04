from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time

class Handler(FileSystemEventHandler):
    def on_modifed(self, event):
        for filename in os.listdir(folder_track):
            file = folder_track + "/" + file_name
            new_path = folder_dest + "/" + file_name
            os.rename(file, new_path)


folder_track = "C:/Users/N1rut/Downloads/test"
folder_dest = "C:/Users/N1rut/Downloads"

handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

try:
    while(True):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()