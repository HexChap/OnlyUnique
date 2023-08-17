import json
import os.path


class Hashes:
    def __init__(self, hashes_path):
        self.hashes_path = hashes_path

        if not os.path.exists(self.hashes_path):
            with open(self.hashes_path, "x") as f:
                f.write("{}")

    def write_new_hash(self, name: str, hash_: str):
        with open(self.hashes_path, "r") as f:
            data = json.loads(f.read())

        data[name.strip("decryptedPartly_")] = hash_

        with open(self.hashes_path, "w") as f:
            f.write(json.dumps(data))

    def get_hashes(self) -> list[str]:
        with open(self.hashes_path, "r") as f:
            data = json.loads(f.read())

        return data.values()

    def is_unique(self, hash_) -> bool:
        if hash_ not in self.get_hashes():
            return True

        return False
