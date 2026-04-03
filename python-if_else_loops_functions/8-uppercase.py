#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if('a' <= str[i] <= 'z'):
            str = str[:i] + chr(ord(str[i]) - 32) + str[i+1:]
    return str
