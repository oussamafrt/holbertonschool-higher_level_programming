#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    else:
        max_value = my_list[0]
        for index in my_list:
            if index > max_value:
                max_value = index
    return (max_value)
