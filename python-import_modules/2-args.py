#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    argm = len(argv)

    if argm == 1:
        print("0 arguments.")
    elif argm == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(argm - 1))

    for index in range(1, len_argv):
        print("{}: {}".format(i, argv[index]))
