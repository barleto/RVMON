import re

codeline = re.compile(" [0-9A-Fa-f]{4}")
header = re.compile("Contents of section")

textSec = False

while(True):
    try:
        line = input()
        if header.match(line) and textSec == False :
            textSec = True
        elif header.match(line) and textSec == True :
            break
        elif textSec == True and codeline.match(line) :
            print(line)
    except EOFError:
        break
