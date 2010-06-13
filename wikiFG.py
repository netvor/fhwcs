#!/usr/bin/python

from globals import MatchStat, unmarshalMatches
from operator import itemgetter

goals=list()
for ms in unmarshalMatches('parsed/match%02d.pkl'):
  if ms.hasResults:
    goals += ms.goals

def wikiFGheader():
  return '^ %-50s ^  Minute  ^' % ('Team')

def wikiFGrow(team, minute):
  return "| %-50s | %7d' |" % (team,minute)

print '\n\n===== Fastest goal =====\n'.encode('utf-8')
print wikiFGheader().encode('utf-8')

for (minute,team) in sorted(goals, key=itemgetter(0))[:10]:
  print wikiFGrow(team,minute).encode('utf-8')
