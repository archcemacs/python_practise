#!/usr/bin/python2

import os
ls = os.linesep

'get file name:'
fobj = open('test.txt', 'w')

all = []
while True:
    entry = raw_input('>>> ')
    if entry == '.':
        break
    else:
        all.append(entry)
fobj.writelines(['%s, %s' % (x, ls) for x in all])

fobj.close()
fobj = open('test.txt', 'r')
for each_line in fobj:
    print each_line.strip()
fobj.close()
print 'Done!'
