import os
from time import sleep

from watchdog.events import FileSystemEventHandler, FileCreatedEvent, DirCreatedEvent

from core import get_file_hash, delete_safe
from hashes import Hashes
from upload import upload

hf = Hashes("hashes.json")


class OnCreatedHandler(FileSystemEventHandler):
    # def on_any_event(self, event):
    #     print(event.event_type, event.src_path)

    def __init__(self, upload_enabled, only_unique):
        self.upload_enabled = upload_enabled
        self.only_unique = only_unique

    def on_created(self, event: FileCreatedEvent | DirCreatedEvent):
        if isinstance(event, DirCreatedEvent):
            return

        hash_ = get_file_hash(event.src_path)
        path = event.src_path.removeprefix(".\\")

        print(f"{path} with hash {hash_} created")

        if hf.is_unique(hash_):
            print(f"{path} is unique")

            if self.upload_enabled:
                upload(path)

            hf.write_new_hash(path, hash_)
            print(f"Written successfully\n")

        else:
            print(f"{path} is not unique.\n")

            if self.only_unique:
                print("Trying delete")
                delete_safe(path)
