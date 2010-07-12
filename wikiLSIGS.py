#!/usr/bin/python

from globals import TeamStat, teamSorted, unmarshal, counter
from optfunc import optfunc
from sys import maxint

def wikiLSIGSheader(prefix):
  if prefix: return '^  #  ^ %-50s ^  Group  ^  GF/GA  ^  GD  ^  Pts  ^' % ('Team')
  else: return '^ %-50s ^  Group  ^  GF/GA  ^  GD  ^  Pts  ^' % ('Team')

def wikiLSIGSrow(ts,prefix):
  gfga = '%d/%d' % (ts.goalsFor, ts.goalsAgainst)
  if prefix: return '| %3d | %-50s |  %5s  |  %-5s  | %4d | %5d |' % (counter.next(),ts.teamWiki(), ts.group.upper(), gfga, ts.goalsDiff, ts.points)
  else: return '| %-50s |  %5s  |  %-5s  | %4d | %5d |' % (ts.teamWiki(), ts.group.upper(), gfga, ts.goalsDiff, ts.points)

def wikiLSIGS(num=10,prefix=False):
  standings = unmarshal('parsed/gss.pkl', maxint)
  print '\n\n==== Lowest score in group stage ====\n'.encode('utf-8')
  print wikiLSIGSheader(prefix).encode('utf-8')
  for row in list(reversed(teamSorted(standings)))[:num]:
    print wikiLSIGSrow(row,prefix).encode('utf-8')

optfunc.main(wikiLSIGS)
