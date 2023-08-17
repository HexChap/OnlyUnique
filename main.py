from watchdog.observers import Observer

from file_event_handler import OnCreatedHandler


event_handler = OnCreatedHandler()
observer = Observer()

observer.schedule(event_handler, path='.', recursive=False)
observer.start()

while True:
    try:
        pass
    except KeyboardInterrupt:
        observer.stop()
