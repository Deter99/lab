import Pyro5.api
from string_service import StringService

def main():
    daemon = Pyro5.api.Daemon()  # Start Pyro daemon
    ns = Pyro5.api.locate_ns()   # Locate the name server
    uri = daemon.register(StringService)  # Register the object
    ns.register("example.stringconcat", uri)  # Register object name in name server

    print("StringService is ready.")
    daemon.requestLoop()  # Start the event loop

if __name__ == "__main__":
    main()
