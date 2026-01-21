#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    count = 0
    while count < x:
        try:
            print("{:d}".format(my_list[count]))
            printed += 1
        except (TypeError, ValueError):
            pass
        count += 1
    return printed
