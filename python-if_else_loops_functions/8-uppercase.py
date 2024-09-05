#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        if char >= 'a' and char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)

