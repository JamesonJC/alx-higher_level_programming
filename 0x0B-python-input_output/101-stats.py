#!/usr/bin/python3
import sys


def print_status():
    ''' Function print the status request '''
    c = 0
    s = 0
    s_c = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    for l in sys.stdin:
        line = l.split()
        try:
            s += int(line[-1])
            c = line[-2]
            s_c[code] += 1
        except:
            continue
        if c == 9:
            print("File size: {}".format(s))
            for key, val in sorted(s_c.items()):
                if (val != 0):
                    print("{}: {}".format(key, val))
            c = 0
        c += 1
    if c < 9:
        print("File size: {}".format(s))
        for key, val in sorted(s_c.items()):
            if (val != 0):
                print("{}: {}".format(key, val))


if __name__ == "__main__":
    print_status()
