import os
from pathlib import Path

from core import conf, get_file_hash, delete_safe
from hashes import Hashes


def check_unique(only_unique: bool = False):
    target_dir = Path(conf["check_unique_dir"])
    hashes_filepath = target_dir / f"{target_dir}-hashes.json"

    with open(hashes_filepath, "w+") as f:
        f.write("{}")

    hashes = Hashes(hashes_filepath)

    files = (file for file in target_dir.iterdir() if file.is_file())

    for i, file in enumerate(files):
        if file == hashes_filepath:
            continue

        if hashes.is_unique(hash_ := get_file_hash(file)):
            print(f"{file} is unique. Writing")
            hashes.write_new_hash(file.name, hash_)

        else:
            print(f"{file} is not unique.")

            if only_unique:
                print("trying delete")
                delete_safe(file)

    print(f"unique files {len(hashes.get_hashes())}/{i}")
