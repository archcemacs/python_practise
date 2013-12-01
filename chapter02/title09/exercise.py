#!/usr/bin/python2

if __name__ == '__main__':
    sum = 0
    temp = [1, 2, 3, 4, 6]
    for i in temp:
        sum += i
    print float(sum) / 5
    print sum // 5
    print sum / float(5)
