#!/usr/bin/python2

if __name__ == '__main__':

    choice = raw_input('w choice while, f choice for, q choice quit:')
    while choice != 'q':
        i = 0
        sum = 0
        if choice == 'w':
            while i < 5:
                num = raw_input('Enter a number:')
                sum += int(num)
                if i == 4:
                    print 'The sum is %d.' % (sum)
                i += 1
        elif choice == 'f':
            sum = 0
            for i in range(5):
                num = raw_input('Enter a number:')
                sum += int(num)
                if i == 4:
                    print 'The sum is %d.' % (sum)
        choice = raw_input('w choice while, f choice for, q choice quit:')
