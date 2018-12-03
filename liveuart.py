#!/usr/bin/python3
import sys
import time

w = open(sys.argv[1], "rb")
r = open(sys.argv[2], "rb")
r.seek(0,2)
w.seek(0,2)
while(True):
    ri = r.read()
    if len(ri) > 0:
        print("R:\t", end="", flush=True)
        for i in range(0, len(ri)):
            print("{:02x}".format(ri[i]), end="", flush=True)
        print("\n", flush=True)
    wi = w.read()
    if len(wi) > 0:
        print("W:\t", end="", flush=True)
        for i in range(0, len(wi)):
            print("{:02x}".format(wi[i]), end="", flush=True)
        print("", flush=True)
