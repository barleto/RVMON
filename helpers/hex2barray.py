
while(True):
    inp = input()
    inp = inp.replace("\n", "")
    inp = inp.replace("0x", "")
    inp = inp.replace(" ", "")
    n = 2
    inp = [inp[i:i+n] for i in range(0, len(inp), n)]
    print("ser.write(b\"", end="");
    for i in range(0, len(inp)):
            print( "\\x{}".format(inp[i]), end="")
    print("\")");
