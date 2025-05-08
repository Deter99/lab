import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
result = proxy.concat(str1, str2)
print("Concatenated result:", result)