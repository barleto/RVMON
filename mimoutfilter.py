while(True):
    try:
        inp = input()
    except EOFError:
        break
    countmin = 0
    countmax = 10
    while countmax <= len(inp):
        fb = inp[countmin:countmin+2]
        fb = "{:b}".format(int(fb,16))
        if fb[1] == '1':#write
            print(inp[countmin:countmax])
            amount = int(fb[2:],2) + 1
            countmin+=10
            countmax+=8
            for i in range (0, amount):
                print("    "+inp[countmin:countmax])
                countmin += 8
                countmax += 8
            countmax+=2
        else:#read
            print(inp[countmin:countmax])
            amount = int(fb[2:],2) + 1
            countmin+=10
            countmax+=8
            for i in range (0, amount):
                print("    "+inp[countmin:countmax])
                countmin += 8
                countmax += 8
            countmax+=2
