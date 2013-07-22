__author__ = 'angrymarmot'
#Approach.

#Randomly generate E, V I events first.
#Randomly generate E, V O events where O > I but less than 1440 for the time value

#eventcount, personlimit, roomlimit, ee, le = argv0, argv1, argv2, argv3, argv4
#events = [[]]
#roomlist = []
#personlist = []
#For r in xrange (eventcount/2):
#    t = rand(ee to 1440)
#    r = rand(0 to roomlimit)
#    p = rand(0 to personlimit)
#    personlist.append(p)
#    roomlist.append(r)
#    events.append([p, r, I, t])
#    t = rand(t to le) (so it's greater than original t)
#    events.append([p, r, O, t])

from sys import argv
import random

eventcount, personlimit, roomlimit, ee, le = int(argv[1]), int(argv[2]), int(argv[3]), int(argv[4]), int(argv[5])
events = [[]]
personlist = [x for x in xrange(personlimit)]
personlist = sorted(personlist)
random.seed()
p = 0
total = 0
for r in xrange(eventcount):
    t = random.randrange(ee, le, 1)
    r = random.randrange(0, roomlimit, 1)
    events.append([p, r, 'I', t])
    total += 1
    t = random.randrange(t, le, 1)
    events.append([p, r, 'O', t])
    total += 1
    p += 1
    if p == (personlimit + 1):
        p = 1
events[0] = [total]
for item in events:
    print str(item).strip('[]')