import hashlib as hl
import json
import os
from os import PathLike
from time import sleep

with open("conf.json", "r") as f:
    conf = json.loads(f.read())


def get_file_hash(filepath: PathLike) -> str:
    try:
        with open(filepath, "rb") as f:
            return hl.md5(f.read()).hexdigest()
    except PermissionError as e:
        if e.errno == 13:
            print(f"{filepath} permission denied. skipping")


def delete_safe(filepath: PathLike):
    for i in range(5):
        try:
            os.remove(filepath)

        except PermissionError as e:
            if e.winerror == 32:  # most likely happens when copy/paste files
                print("file is used by another process. Sleeping and then retrying")
                sleep(1)
            elif e.winerror == 5:
                print("access denied. restart with elevated perms. skipping")
                break

            continue

        print("deleted\n")
        break
