#!/usr/bin/python

from globals import TeamStat, teamSorted, unmarshal

standings = unmarshal('parsed/gss.pkl')

def wikiLSIGSheader():
  return '^ %-50s ^  Group  ^  GF/GA  ^  GD  ^  Pts  ^' % ('Team')

def wikiLSIGSrow(ts):
  gfga = '%d/%d' % (ts.goalsFor, ts.goalsAgainst)
  return '| %-50s |  %5s  |  %-5s  | %4d | %5d |' % (ts.teamWiki(), ts.group.upper(), gfga, ts.goalsDiff, ts.points)

print '\n\n==== Lowest score in group stage ====\n'.encode('utf-8')
print wikiLSIGSheader().encode('utf-8')
for row in list(reversed(teamSorted(standings)))[:10]:
  print wikiLSIGSrow(row).encode('utf-8')
