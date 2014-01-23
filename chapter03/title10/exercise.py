#!/usr/bin/python2
'Create text file.'

import os
ls = os.linesep

# get file name:
while True:
    file_name = raw_input('Input the file\'s name: ')
    try:
        open (file_name, 'r')
        print "Error ,%s is already existing." % file_name
    except IOError:
        break
        file_name.close()
all = []
print "Enter '.' to quit."
while True:
    entry = raw_input('>>>')
    if entry == '.':
        break
    else:
        all.append (entry)
file_object = open(file_name, 'w')
file_object.writelines(['%s, %s' % (x, ls) for x in all])
file_object.close()
print 'Done!'
