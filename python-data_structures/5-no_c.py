#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for idx in my_string:
        if idx != "c" and idx != "C":
            string += idx
    return string
