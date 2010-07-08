#!/usr/bin/python

from globals import MatchStat, unmarshalMatches
from operator import itemgetter
from optfunc import optfunc

def wikiMGSheader():
  return '^ %-50s ^  Goals scored  ^  Goals against  ^' % ('Team')

def wikiMGSrow(team, goals):
  gf='**%d**' % (goals[0])
  return '| %-50s | %14s | %15d |' % (team,gf,-goals[1])

def wikiMGS(num=10):
  mgs=dict()
  for ms in unmarshalMatches('parsed/match%02d.pkl'):
    if ms.hasResults:
      for team in [ms.homeWiki(), ms.awayWiki()]: 
        if team not in mgs: mgs[team] = [0,0]
      mgs[ms.homeWiki()][0] += len(ms.homeGoals)
      mgs[ms.awayWiki()][0] += len(ms.awayGoals)
      mgs[ms.awayWiki()][1] -= len(ms.homeGoals)
      mgs[ms.homeWiki()][1] -= len(ms.awayGoals)

  print '\n\n==== Most goals scored ====\n'.encode('utf-8')
  print wikiMGSheader().encode('utf-8')

  for (team,goals) in list(reversed(sorted(mgs.items(), key=itemgetter(1))))[:num]:
    print wikiMGSrow(team,goals).encode('utf-8')

optfunc.main(wikiMGS)
