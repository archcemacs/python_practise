#!/usr/bin/python2

if __name__ == '__main__':
    a = raw_input('Enter a number:')
    num = int(a)
    if num > 0:
        print '%d > 0' % (num)
    elif num < 0:
        print '%d < 0' % (num)
    else:
        print '%d = 0' % (num)

