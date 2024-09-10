#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for index in set(my_list):
        result += index
    return (result)
