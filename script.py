import sys
import requests

# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


# print(greet("World"))
# print(greet("Gisael"))

r = requests.get("https://www.rokogrill.com")
print(r.status_code)
