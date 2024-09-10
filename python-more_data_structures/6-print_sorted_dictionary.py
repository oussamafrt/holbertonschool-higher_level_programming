#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dictionary = sorted(a_dictionary)
    for index in new_dictionary:
        print("{}: {}".format(index, a_dictionary[index]))
