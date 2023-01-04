import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
form_dir = "C:/User/User/Desktop"
to_dir = "C:/Users/User/Desktop/New folder (3)"
#Event Handler Class
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")
    
    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")
    
    def on_modified(self, event):
        print(f"The {event.src_path} has bee modified successfully!")

    def on_moved(self, event):
        print(f"The {event.src_path} has been moved safely")

#intilize event handler class
event_handler = FileEventHandler()
#initilise observer
observer = Observer()
#schedule the observer
observer.schedule(event_handler,recursive = True)
#start the observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running....")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()