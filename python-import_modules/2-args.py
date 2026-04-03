#!/usr/bin/python3
str = input()
argv = str.split()
if len(argv) == 1:
    print("1 argument:")
else:
    print(f"{len(argv)} arguments:")
for i in range(len(argv)):
    print(f"{i + 1}: {argv[i]}")
