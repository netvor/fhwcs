#!/usr/bin/python

from globals import MatchStat, unmarshalMatches
from operator import attrgetter

matches=list()
for ms in unmarshalMatches('parsed/match%02d.pkl'):
  if ms.hasResults:
    ms.totalGoals = len(ms.homeGoals) + len(ms.awayGoals)
    matches.append(ms)

def wikiMGPGheader():
  return '^  No.  ^       When       ^  %-88s  ^  Goals scored  ^' % ('Match')

def wikiMGPGrow(ms):
  if len(ms.group) == 1: ms.group = 'Group '+ms.group
  match = '%s: %s //vs.// %s' % (ms.group, ms.homeWiki, ms.awayWiki)
  _goals = '**%d** (%d:%d)' % (ms.totalGoals, len(ms.homeGoals), len(ms.awayGoals))
  return '| %5d | %16s | %-90s | %-14s |' % (ms.number, ms.when, match, _goals)

print '\n\n==== Most goals per game ====\n'.encode('utf-8')
print wikiMGPGheader().encode('utf-8')

for ms in list(reversed(sorted(matches,key=attrgetter('totalGoals'))))[:10]:
  print wikiMGPGrow(ms).encode('utf-8')
