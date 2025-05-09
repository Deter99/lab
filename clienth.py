import Pyro5.api

# Use the URI printed by the server
uri = input("Enter the server URI (e.g., PYRO:obj_...): ")
string_service = Pyro5.api.Proxy(uri)     # Connect to remote object

# Send strings to server
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

result = string_service.concatenate(s1, s2)
print("Concatenated result from server:",result)