# repeats_check.py
#
"""
A little script to check how many names one can expect to get without
hitting repeats. Obviously this could be done using math, but
(unsatisfying excuses here).
"""

import cumberbatch

first_names = []
while True:
    name = cumberbatch.first()
    if name in first_names:
        break
    else:
        first_names.append(name)
print 'Generated {} clean first names before a repeat appeared.'.format(len(first_names))

last_names = []
while True:
    name = cumberbatch.last()
    if name in last_names:
        break
    else:
        last_names.append(name)
print 'Generated {} clean last names before a repeat appeared.'.format(len(last_names))

full_names = []
while True:
    name = cumberbatch.full()
    if name in full_names:
        break
    else:
        full_names.append(name)
print 'Generated {} clean full names before a repeat appeared.'.format(len(full_names))
