#!/usr/bin/python2
if __name__ == '__main__':
    string = raw_input('Enter a string:')
    i = 0
    while i<len(string):
        print string[i]
        i += 1
    for i in string:
        print i
