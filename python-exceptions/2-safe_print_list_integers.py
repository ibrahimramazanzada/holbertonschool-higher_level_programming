#!/usr/bin/python3
"""Print integers from a list safely."""


def safe_print_list_integers(my_list=[], x=0):
    """Print integer values from the first x elements of a list."""
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
