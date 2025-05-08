import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8003/")
#number = 5
#result = proxy.factorial(number)
#print(f"The factorial of {number} is {result}")
n = input("Enter an integer to compute factorial: ")
try:
    num = int(n)
    result = proxy.factorial(num)
    print(f"Factorial of {num} is {result}")
except ValueError:
    print("Please enter a valid integer or 'exit'.")