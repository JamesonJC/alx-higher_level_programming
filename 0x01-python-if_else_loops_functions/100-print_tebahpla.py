#!/usr/bin/python3

for c in range(ord('z'), ord('a') - 1, -1):
    i = 32 - i
    print(chr(c - i), end="")
