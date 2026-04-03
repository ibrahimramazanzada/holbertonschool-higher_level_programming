#!/usr/bin/python3
def islower(c):
    if not c:
        raise ValueError("empty string")
    return 'a' <= c <= 'z'
