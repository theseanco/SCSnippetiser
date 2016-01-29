# This works for checking a line for a particular pattern

import re
from time import sleep

# open Osc file as an example
classlib = open('files/Osc.sc')

# regex to find the kubes containing classes
classseparator = re.compile(" : ")
ar = re.compile("ar")

while True:
    line = classlib.readline()
    # checks if the Class : Type string matches
    check = re.search(classseparator, line)
    if check:
        # grabs classname and reads following line
        classname = line.split(' ', 1)[0]
        print classname
        # TODO: add classname to snippet
        line = classlib.readline()
        # checks if the method is correct
        check = re.search(ar, line)
        if check:
            # TODO: add a .ar option to the snippet
            line = classlib.readline()
            # check if this is actually the end of the line
            if line.find(";") != -1:
                snippetline = line.replace('=', ':')
                snippetline = snippetline.replace('arg ', '(')
                snippetline = snippetline.replace(';', ')')
            else:
                print 'exceptional string'
                # create a duplicate of the previous line, then read a new one
                # to the same string, then parse again and see what happens
                line2 = line
                line = classlib.readline()
                line2 = line2 + line
                snippetline = line2.replace('=', ':')
                snippetline = snippetline.replace('arg ', '(')
                snippetline = snippetline.replace(';', ')')
            print snippetline
    sleep(0.01)
