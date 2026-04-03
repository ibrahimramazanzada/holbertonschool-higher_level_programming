#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # exclude the script name itself
    count = len(argv)

    if count == 1:
        label = "argument"
    else:
        label = "arguments"

    if count == 0:
        separator = "."
    else:
        separator = ":"

    print(f"{count} {label}{separator}")

    for i in range(count):
        print(f"{i + 1}: {argv[i]}")
