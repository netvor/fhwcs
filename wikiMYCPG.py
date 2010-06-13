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
  if len(ms.group) == 1: ms.group = 'Group '+ms.group
  match = '%s: %s //vs.// %s' % (ms.group, ms.homeWiki, ms.awayWiki)
  _yellow = '%d (%d:%d)' % (ms.homeCards[0]+ms.awayCards[0], ms.homeCards[0], ms.awayCards[0])
  _yyr = '%d (%d:%d)' % (ms.homeCards[1]+ms.awayCards[1], ms.homeCards[1], ms.awayCards[1])
  _red = '%d (%d:%d)' % (ms.homeCards[2]+ms.awayCards[2], ms.homeCards[2], ms.awayCards[2])
  _total = '**%d** (%d:%d)' % (ms.homeCards[3]+ms.awayCards[3], ms.homeCards[3], ms.awayCards[3])
  return '| %5d | %16s | %-90s | %-12s | %-12s | %-12s | %-16s |' % (ms.number, ms.when, match, _yellow, _yyr, _red, _total)

print '\n\n==== Most yellow cards per game ====\n'.encode('utf-8')
print wikiMYCPGheader().encode('utf-8')

for ms in list(reversed(sorted(matches,key=attrgetter('totalCards'))))[:10]:
  print wikiMYCPGrow(ms).encode('utf-8')
