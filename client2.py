import Pyro5.api

def main():
    uri = Pyro5.api.locate_ns().lookup("example.stringconcat")
    string_service = Pyro5.api.Proxy(uri)

    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    result = string_service.concatenate(str1, str2)
    print("Concatenated result:", result)

if __name__ == "__main__":
    main()
