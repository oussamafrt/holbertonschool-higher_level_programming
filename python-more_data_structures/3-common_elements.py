#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = []
    for idx1 in set_1:
        for idx2 in set_2:
            if idx1 == idx2:
                new_list.append(idx1)
    return (new_list)
