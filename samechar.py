import sys
f1 = open(sys.argv[1], "r").read()
f2 = open(sys.argv[2], "r").read()

f1 = f1.replace("\n","")
f2 = f2.replace("\n","")
l1 = len(f1)
l2 = len(f2)

for i in range(0, max(l1, l2)):
    if   i < min(l1, l2):
        if f1[i] == f2[i]:
            print(f1[i], end="", flush=True)
        else:
            print("T", end="")
    else:
        print("Z", end="")
