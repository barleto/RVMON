import json
import sys
import re

print(" ")
with open(sys.argv[1]) as f:
    map = json.load(f)

def translateCommand(com):
    for key in map:
        if re.match(map[key], com):
            print("<<<< {} ({})".format(key, com[0:25]))
            return
    print("< {}".format(com))

while(True):
    try:
        inp = input()
    except EOFError:
        continue
    if(len(inp) <= 1):
        continue
    if(inp[0] == ">"):
        print(  inp)
        continue
    c = inp.partition("|")[0][1:]
    c = c.replace(" ", "")
    translateCommand(c)
