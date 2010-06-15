#!/usr/bin/python

from globals import MatchStat, getInFile, marshal, unmarshal
import re

report=unmarshal('')
ms=unmarshal('parsed/match%02d.pkl'%(report['number']),None)

print ("Import match report for match %d: %s vs. %s (%s)" % (ms.number, ms.homeName, ms.awayName, ms.when)).encode('utf-8')

assert(ms.homeCode == report['homeCode'])
assert(ms.awayCode == report['awayCode'])
#assert(ms.homeName == report['homeName'])
#assert(ms.awayName == report['awayName'])

ms.goals      = report['goals']
ms.homeGoals  = report['homeGoals']
ms.awayGoals  = report['awayGoals']
ms.homeCards  = report['homeCards']
ms.awayCards  = report['awayCards']
ms.hasResults = True

res = '%d:%d' % (len(ms.homeGoals),len(ms.awayGoals))
try: fg="%d' -- %s" % (min(ms.goals)[0],min(ms.goals)[1])
except: fg='(no goals)'
print ( "Results of match %d:\n  %s:%s  %s\n  cards: %s : %s\n  first goal: %s" % ( 
  ms.number,
  ms.homeCode,
  ms.awayCode,
  res,
  '/'.join([str(c) for c in ms.homeCards]),
  '/'.join([str(c) for c in ms.awayCards]),
  fg ) ).encode('utf-8')

marshal(ms,'parsed/match%02d.pkl'%(ms.number),None)
