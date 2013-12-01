#!/usr/bin/python2

def sum(arg):
    i = 0
    sum = 0
    while i < len(arg):
        sum += arg[i]
        i += 1
    return sum
def average(arg):
    i = 0
    sum = 0
    while i < len(arg):
        sum += arg[i]
        i += 1
    return float(sum) / len(arg)
if __name__ == '__main__':
    temp = [1, 2, 3, 4, 5, 6]
    choice = raw_input('Enter a 1(sum) or 2(average) or x(quit):')
    while choice != 'x':
        if choice == '1':
            print sum(temp)
        elif choice == '2':
            print average(temp)
        elif choice == 'x':
            pass
        else:
            print 'Entered is wrong.'
        choice = raw_input('Enter a 1(sum) or 2(average) or x(quit):')

