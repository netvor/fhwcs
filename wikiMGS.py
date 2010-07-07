﻿#!/usr/bin/python

from globals import MatchStat, unmarshalMatches
from operator import itemgetter
from optfunc import optfunc

def wikiMGSheader():
  return '^ %-50s ^  Goals scored  ^' % ('Team')

def wikiMGSrow(team, goals):
  return '| %-50s | %14d |' % (team,goals)

def wikiMGS(num=10):
  mgs=dict()
  for ms in unmarshalMatches('parsed/match%02d.pkl'):
    if ms.hasResults:
      for team in [ms.homeWiki(), ms.awayWiki()]: 
        if team not in mgs: mgs[team] = 0
      mgs[ms.homeWiki()] += len(ms.homeGoals)
      mgs[ms.awayWiki()] += len(ms.awayGoals)

  print '\n\n==== Most goals scored ====\n'.encode('utf-8')
  print wikiMGSheader().encode('utf-8')

  for (team,goals) in list(reversed(sorted(mgs.items(), key=itemgetter(1))))[:num]:
    print wikiMGSrow(team,goals).encode('utf-8')

optfunc.main(wikiMGS)
