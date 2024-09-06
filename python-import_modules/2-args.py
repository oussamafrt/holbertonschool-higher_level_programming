#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = sys.argv

    if len(arguments) == 1:
        print("0 arguments")
    elif len(arguments) == 2:
        print("1 argument")
    else:
        print("{} arguments".format(len(arguments) - 1))

    for index in range(1, len(arguments)):
        print("{}: {}".format(index, arguments[index]))
