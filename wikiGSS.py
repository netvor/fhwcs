#!/usr/bin/python

from globals import TeamStat, teamSorted, unmarshal
import string
from collections import deque

standings = unmarshal('parsed/gss.pkl')

def wikiGSSheader(letter):
  return '^ //Group %s://%38s ^  %-2s  ^  %-8s  ^  %-5s  ^  %-2s  ^  %-3s  ^' % (letter.upper(),' ','MP','W/D/L','GF/GA','GD','Pts')

def wikiGSSrow(ts):
  wdl = '%d/%d/%d' % (ts.wins,ts.draws,ts.losses)
  gfga = '%d/%d' % (ts.goalsFor, ts.goalsAgainst)
  return '| %-50s | %4d |  %-8s  |  %-5s  | %4d | %5d |' % (ts.teamWiki(), ts.played, wdl, gfga, ts.goalsDiff, ts.points)

wikiGSSdata=deque()

for letter in string.ascii_uppercase[:8]:
  group=[ wikiGSSheader(letter) ]
  for row in teamSorted(filter(lambda ts: ts.group==letter,standings)):
    group.append(wikiGSSrow(row))
  wikiGSSdata.append(group)

print '\n\n===== Final Standings =====\n\n'.encode('utf-8')

while len(wikiGSSdata) >= 2:
  a=wikiGSSdata.popleft()
  b=wikiGSSdata.popleft()
  print (a[0] + '     ' + b[0]).encode('utf-8')
  print (a[1] + ' ::: ' + b[1]).encode('utf-8')
  print (a[2] + ' ::: ' + b[2]).encode('utf-8')
  print (a[3] + ' ::: ' + b[3]).encode('utf-8')
  print (a[4] + ' ::: ' + b[4]).encode('utf-8')
