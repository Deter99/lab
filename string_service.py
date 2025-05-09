import Pyro5.api

@Pyro5.api.expose
class StringService:
    def concatenate(self, str1, str2):
        print(f"Received strings: '{str1}' and '{str2}'")
        return str1 +' '+ str2