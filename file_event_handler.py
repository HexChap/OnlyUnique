import hashlib as hl
import os

from watchdog.events import FileSystemEventHandler, FileCreatedEvent

from hashes_file import Hashes

hf = Hashes("hashes.json")


def get_file_hash(filepath: str) -> str:
    with open(filepath, "rb") as f:
        return hl.md5(f.read()).hexdigest()


class OnCreatedHandler(FileSystemEventHandler):
    # def on_any_event(self, event):
    #     print(event.event_type, event.src_path)

    def on_created(self, event: FileCreatedEvent):
        path = event.src_path
        hash_ = get_file_hash(path)

        print(f"{path} with hash {hash_} created")

        if hf.is_unique(hash_):
            hf.write_new_hash(path.strip(".\\decryptedPartly_"), hash_)  # decryptedPartly_ is personal, can be deleted
            print(f"{path} is unique and written in the hashes file\n")

        else:
            os.remove(path)
            print(f"{path} is not unique and is being deleted\n")
