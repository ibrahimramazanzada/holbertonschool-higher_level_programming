#!/usr/bin/python3
def uppercase(str):
    upper_str = ''.join(chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in str)
    print("{}".format(upper_str))
