# This works for checking a line for a particular pattern

import re
from time import sleep

# open Osc file as an example
classlib = open('files/Osc.sc')

# regex to find the kubes containing classes
regex = re.compile(" : ")

while True:
    line = classlib.readline()
    # checks if the Class : Type string matches
    check = re.search(regex, line)
    if check:
        # grabs classname and reads following line
        classname = line.split(' ', 1)[0]
        print classname
    sleep(0.1)
