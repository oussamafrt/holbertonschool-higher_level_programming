#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arguments = len(argv)

    if len(arguments) <= 1:
        print("0 arguments")
    else:
        print("{} arguments".format(len(arguments) - 1))

    for index in range(1, len(arguments)):
        print("{}: {}".format(index, arguments[index]))
