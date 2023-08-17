import hashlib as hl
import os
from multiprocessing import Process

from watchdog.events import FileSystemEventHandler, FileCreatedEvent

from hashes import Hashes
from upload import upload

hf = Hashes("hashes.json")


def get_file_hash(filepath: str) -> str:
    with open(filepath, "rb") as f:
        return hl.md5(f.read()).hexdigest()


class OnCreatedHandler(FileSystemEventHandler):
    # def on_any_event(self, event):
    #     print(event.event_type, event.src_path)

    def on_created(self, event: FileCreatedEvent):
        hash_ = get_file_hash(event.src_path)
        path = event.src_path.strip(".\\")

        print(f"{path} with hash {hash_} created")

        if hf.is_unique(hash_):
            print(f"{path} is unique. Upload is starting")
            upload(path)
            hf.write_new_hash(path, hash_)
            print(f"Written successfully\n")

        else:
            os.remove(path)
            print(f"{path} is not unique and is deleted\n")
