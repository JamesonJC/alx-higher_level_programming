#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    sum_args = 0
    for idx in range(len(sys.argv) - 1):
        sum_args += int(sys.argv[idx + 1])
    print("{:d}".format(sum_args))
