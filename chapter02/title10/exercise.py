#!/usr/bin/python2
def print_hello():
    print 'hello world!'
if __name__ == '__main__':
    print_hello()
    i = 1
    num = raw_input('Enter a number between 1 and 100:')
    while i == 1:
        if int(num) > 1 and int(num) < 100:
            print 'You entered %d.' % (int(num))
            print 'You are right.'
            i = 0
        else:
            print 'Eror, You entered %d.' % (int(num))
            num = raw_input('Enter a number between 1 and 100:')
