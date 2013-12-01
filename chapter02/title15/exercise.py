#!/usr/bin/python2
def mysort(*arg_temp):
    arg = list(arg_temp)
    a = arg[0]
    print 'The lenght is %d.' % (len(arg_temp))
    for i in range(len(arg)):
        if a > arg[i]:
            (a, arg[i]) = (arg[i], a)
    return arg
if __name__ == '__main__':
    a = raw_input('Enter the first  number:')
    b = raw_input('Enter the second number:')
    c = raw_input('Enter the third  number:')
    print mysort(a, b, c)
