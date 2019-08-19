import math
import sys
from os import rename

import requests


import rename

print(sys.version)
print(sys.executable)
# testing


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Corey"))

r = requests.get("https://coreyms.com")
print(r.status_code)
