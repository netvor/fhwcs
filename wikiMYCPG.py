#!/usr/bin/python

from globals import MatchStat, unmarshalMatches
from operator import attrgetter

matches=list()
for ms in unmarshalMatches('parsed/match%02d.pkl'):
  if ms.hasResults:
    ms.totalCards = ms.homeCards[2]+ms.awayCards[2]
    matches.append(ms)

def wikiMYCPGheader():
  return '^  No.  ^       When       ^  %-88s  ^  Yellow cards  ^  Direct red cards  ^      Total      ^' % ('Match')

def wikiMYCPGrow(ms):
  if len(ms.group) == 1: ms.group = 'Group '+ms.group
  match = '%s: %s //vs.// %s' % (ms.group, ms.homeWiki, ms.awayWiki)
  _yellow = '%d (%d:%d)' % (ms.homeCards[0]+ms.awayCards[0], ms.homeCards[0], ms.awayCards[0])
  _red = '%d (%d:%d)' % (ms.homeCards[1]+ms.awayCards[1], ms.homeCards[1], ms.awayCards[1])
  _total = '**%d** (%d:%d)' % (ms.homeCards[2]+ms.awayCards[2], ms.homeCards[2], ms.awayCards[2])
  return '| %5d | %16s | %-90s | %-14s | %-18s | %-15s |' % (ms.number, ms.when, match, _yellow, _red, _total)

print '\n\n===== Most yellow cards per game =====\n'.encode('utf-8')
print wikiMYCPGheader().encode('utf-8')

for ms in list(reversed(sorted(matches,key=attrgetter('totalCards'))))[:10]:
  print wikiMYCPGrow(ms).encode('utf-8')
