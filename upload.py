import json

import pysftp


def create_conn() -> pysftp.Connection:
    with open("sftp_conf.json", "r") as f:
        data = json.loads(f.read())

    return pysftp.Connection(
        host=data["host"],
        username=data["username"],
        password=data["password"],
        port=data["port"],
    )


def upload(filepath: str):
    with create_conn() as conn:
        print(f"Uploading {filepath}")
        conn.put(filepath, filepath)
        print(f"Uploaded successfully")
