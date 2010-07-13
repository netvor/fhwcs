#!/usr/bin/python

from globals import MatchStat, getInFile, marshal, unmarshal
import re

ms=unmarshal('')

print "Editing match %d: %s vs. %s (%s)" % (ms.number, ms.homeName, ms.awayName, ms.when)

_homeGoals = raw_input('Goals scored by %s (write the minute of each goal, separated by spaces): ' % ms.homeName).split()
_awayGoals = raw_input('Goals scored by %s (write the minute of each goal, separated by spaces): ' % ms.awayName).split()
_homeCards = raw_input('Yellow, 2Y=R and red cards given to %s (separate three values by spaces): ' % ms.homeName).split()
_awayCards = raw_input('Yellow, 2Y=R and red cards given to %s (separate three values by spaces): ' % ms.awayName).split()

homeGoals = list()
awayGoals = list()
homeCards = [0,0,0]
awayCards = [0,0,0]

for g in _homeGoals:
  m = int(g)
  homeGoals.append(m)
for g in _awayGoals:
  m = int(g)
  awayGoals.append(m)

try:
  homeCards[0] = int(_homeCards[0])
  homeCards[1] = int(_homeCards[1])
  homeCards[2] = int(_homeCards[2])
except IndexError:
  pass
try:
  awayCards[0] = int(_awayCards[0])
  awayCards[1] = int(_awayCards[1])
  awayCards[2] = int(_awayCards[2])
except IndexError:
  pass
homeCards = tuple(homeCards + [homeCards[0] + 3 * homeCards[1] + 4 * homeCards[2]])
awayCards = tuple(awayCards + [awayCards[0] + 3 * awayCards[1] + 4 * awayCards[2]])

goals=list()
for g in homeGoals:
  goals.append((g,ms.homeCode))
for g in awayGoals:
  goals.append((g,ms.awayCode))

ms.goalsCode=goals
ms.homeGoals = homeGoals
ms.awayGoals = awayGoals
ms.homeCards = homeCards
ms.awayCards = awayCards
ms.hasResults = True

res = '%d:%d' % (len(homeGoals),len(awayGoals))
try: fg="%d' -- %s" % min(goals)
except: fg='(no goals)'
ycrc = '%d/%d : %d/%d -- total: %d' % (homeCards[0],homeCards[1],awayCards[0],awayCards[1],homeCards[2]+awayCards[2])
print "Results of match %d:\n  %s:%s  %s\n  yc/rc: %s\n  first goal: %s" % (ms.number,ms.homeCode,ms.awayCode,res,ycrc,fg)

marshal(ms,'parsed/match%02d.pkl'%(ms.number))
