import sys
f1 = open(sys.argv[1], "rb").read()
f2 = open(sys.argv[2], "rb").read()

for i in range(0, min(len(f1), len(f2))):
    if f1[i] == f2[i]:
        print("0x%X  " % (f1[i]), end="", flush=True)
    else:
        print("0x**  ", end="")
