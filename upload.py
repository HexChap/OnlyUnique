import json

import pysftp

from core import conf


def create_conn() -> pysftp.Connection:
    cred = conf["sftp"]

    return pysftp.Connection(
        host=cred["host"],
        username=cred["username"],
        password=cred["password"],
        port=cred["port"],
    )


def upload(filepath: str):
    with create_conn() as conn:
        print(f"Uploading {filepath}")
        conn.put(filepath, filepath)
        print(f"Uploaded successfully")
