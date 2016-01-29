# This works for checking a line for a particular pattern

import re
from time import sleep

# open Osc file as an example
classlib = open('files/Osc.sc')

# regex to find the kubes containing classes
classseparator = re.compile(" : ")
ar = re.compile("ar")

f = open('test.snippets', 'w')

while True:
    line = classlib.readline().lstrip()
    # checks if the Class : Type string matches
    check = re.search(classseparator, line)
    if check:
        # grabs classname and reads following line
        classname = line.split(' ', 1)[0]
        print classname
        print ('snippet'+classname.lower()+' "'+classname+'" '+'i')
        # TODO: add classname to snippet
        line = classlib.readline().strip()
        # checks if the method is correct
        check = re.search(ar, line)
        if check:
            # TODO: add a .ar option to the snippet
            line = classlib.readline().strip()
            # check if this is actually the end of the line
            if line.find(";") != -1:
                # slightly format the string for sclang-friendly application
                snippetline = line.replace('=', ':')
                snippetline = snippetline.replace('arg ', '(')
                snippetline = snippetline.replace(';', '')
                snippetline = str.split(snippetline, ',')
                # create opening bracked to encase formatted 'snippetted' args
                formatted = '('
                # start at 2 to account for .ar or .kr discintction
                i = 2
                for item in snippetline:
                    # put it all in a string, i giving it snippet numbers
                    formatted += '${' + str(i) + ':'
                    formatted += item
                    formatted += '}, '
                    i = i + 1
                formatted += ')'
            else:
                print 'exceptional string'
                # create a duplicate of the previous line, then read a new one
                # to the same string, then parse again and see what happens
                # only for longer strings
                line2 = line
                line = classlib.readline().strip()
                line2 = line2 + line
                # once the lines are joined, perform the same as above
                snippetline = line2.replace('=', ':')
                snippetline = snippetline.replace('arg ', '(')
                snippetline = snippetline.replace(';', ')')
                formatted = '('
                i = 2
                for item in snippetline:
                    formatted += '${' + str(i) + ':'
                    formatted += item
                    formatted += '}, '
                    i = i + 1
                formatted += ')'
            print formatted
    sleep(0.01)
