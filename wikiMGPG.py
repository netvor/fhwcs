#!/usr/bin/python

from globals import MatchStat, unmarshalMatches
from operator import attrgetter
from optfunc import optfunc

def wikiMGPGheader():
  return '^  No.  ^       When       ^  %-88s  ^  Goals scored  ^' % ('Match')

def wikiMGPGrow(ms):
  _goals = '**%d** (%d:%d)' % (ms.totalGoals, len(ms.homeGoals), len(ms.awayGoals))
  return '| %5d | %16s | %-90s | %-14s |' % (ms.number, ms.when, ms.matchTitle(), _goals)

def wikiMGPG(num=10):
  matches=list()
  for ms in unmarshalMatches('parsed/match%02d.pkl'):
    if ms.hasResults:
      ms.totalGoals = len(ms.homeGoals) + len(ms.awayGoals)
      matches.append(ms)

  print '\n\n==== Most goals per game ====\n'.encode('utf-8')
  print wikiMGPGheader().encode('utf-8')

  for ms in list(sorted( sorted(matches,key=lambda x:x.when_tm()) ,key=attrgetter('totalGoals'), reverse=True))[:num]:
    print wikiMGPGrow(ms).encode('utf-8')

optfunc.main(wikiMGPG)
