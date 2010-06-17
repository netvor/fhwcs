#!/usr/bin/python

from globals import MatchStat, unmarshalMatches
from operator import attrgetter

matches=list()
for ms in unmarshalMatches('parsed/match%02d.pkl'):
  if ms.hasResults:
    ms.totalCards = ms.homeCards[3]+ms.awayCards[3]
    matches.append(ms)

def wikiMYCPGheader():
  return '^  No.  ^       When       ^  %-88s  ^    Yellow    ^     2Y=R     ^  Direct red  ^  Weighted Total  ^' % ('Match')

def wikiMYCPGrow(ms):
  _yellow = '%d (%d:%d)' % (ms.homeCards[0]+ms.awayCards[0], ms.homeCards[0], ms.awayCards[0])
  _yyr = '%d (%d:%d)' % (ms.homeCards[1]+ms.awayCards[1], ms.homeCards[1], ms.awayCards[1])
  _red = '%d (%d:%d)' % (ms.homeCards[2]+ms.awayCards[2], ms.homeCards[2], ms.awayCards[2])
  _total = '**%d** (%d:%d)' % (ms.homeCards[3]+ms.awayCards[3], ms.homeCards[3], ms.awayCards[3])
  return '| %5d | %16s | %-90s | %-12s | %-12s | %-12s | %-16s |' % (ms.number, ms.when, ms.matchTitle(), _yellow, _yyr, _red, _total)

print '\n\n==== Most yellow cards per game ====\n'.encode('utf-8')
print wikiMYCPGheader().encode('utf-8')

for ms in list(sorted( sorted(matches,key=attrgetter('when')) ,key=attrgetter('totalCards'), reverse=True))[:10]:
#for ms in list(reversed(sorted(matches,key=attrgetter('totalCards'))))[:10]:
  print wikiMYCPGrow(ms).encode('utf-8')
