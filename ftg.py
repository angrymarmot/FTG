__author__ = 'angrymarmot'

#Approach.

# Randomly generate E, V I events first.
# Randomly generate E, V O events where O > I but less than 1440 for the time value

# events = [[]]
# For r in xrange (e/2):
   # t = rand(0 to 1440)
  #  r = rand(0 to 100)
   # events.append([p, r, I, t])
   # t = rand(t to 1440) (so it's greater than original t)
   # events.append([p, r, O, t])
#
#
from sys import argv

events = [[]]

