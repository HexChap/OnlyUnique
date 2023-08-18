import os

from watchdog.observers import Observer

from check_unique import check_unique
from file_event_handler import OnCreatedHandler


def observe(
    upload_enabled: bool = False,
    only_unique: bool = False
):
    event_handler = OnCreatedHandler(upload_enabled, only_unique)
    observer = Observer()

    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    while True:
        try:
            pass
        except KeyboardInterrupt:
            observer.stop()


if __name__ == '__main__':
    choice = input("1.Observe root\n2.Check targeted folder (conf.json)\n--> ")
    is_only_unique = True if input("Leave only unique files? (y/n)\n--> ") in ["y", "yes", "1"] else False

    if choice == "1":
        is_upload_enabled = input("Enable uploading? (sftp section in conf.json must be filled) (y/n) --> ")

        print("\nObserving...\n")
        observe(
            upload_enabled=True if is_upload_enabled in ["y", "yes", "1"] else False,
            only_unique=is_only_unique
        )

    else:
        check_unique(
            only_unique=is_only_unique
        )
