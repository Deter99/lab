from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
server = SimpleXMLRPCServer(("localhost", 8003))
print("Server is running on port 8003...")
server.register_function(factorial, "factorial")
server.serve_forever()