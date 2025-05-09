import Pyro5.api

@Pyro5.api.expose
class StringService:
    def concatenate(self, s1, s2):
        return s1 + s2

def main():
    daemon = Pyro5.api.Daemon()                      # Create a Pyro server
    uri = daemon.register(StringService)             # Register the class
    print("Server is ready. Object URI =", uri)      # Print URI for client use
    daemon.requestLoop()                             # Start event loop

if _name_ == "main":
    main()