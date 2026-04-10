#!/usr/bin/python3
"""Print integers from a list safely."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements and return the count of integers."""
    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except TypeError:
            continue
    print()

    return count
