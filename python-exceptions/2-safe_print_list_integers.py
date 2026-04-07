#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            element = my_list[i]
            if isinstance(element, int) and not isinstance(element, bool):
                print("{:d}".format(element), end="")
                count += 1
        print()
    except (IndexError, ValueError):
        print()
    return count
