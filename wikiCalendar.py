#!/usr/bin/python

from globals import MatchStat, unmarshalMatches

matches = unmarshalMatches('parsed/match%02d.pkl')

def wikiCALheader():
  return '^  No.  ^       When       ^  %-88s  ^   Score   ^  Weighted Cards  ^        First Goal        ^' % ('Match')

def wikiCALrow(ms):
  if ms.hasResults:
    results = '%d:%d' % (len(ms.homeGoals),len(ms.awayGoals))
    try: firstgoal="**%d'** -- %s" % (min(ms.goals)[0],min(ms.goals)[1])
    except: firstgoal='//(no goals)//'
    ycrc = '**%d** (%d:%d)' % (ms.homeCards[3]+ms.awayCards[3], ms.homeCards[3], ms.awayCards[3])
  else:
    results=''
    ycrc=''
    firstgoal=''
  if len(ms.group) == 1: ms.group = 'Group '+ms.group
  match = '%s: %s //vs.// %s' % (ms.group, ms.homeWiki, ms.awayWiki)
  return '| %5d | %16s | %-90s |  %7s  |  %-14s  | %-24s |' % (ms.number, ms.when, match, results, ycrc, firstgoal)

print '\n\n===== Calendar =====\n'.encode('utf-8')
print wikiCALheader().encode('utf-8')

for ms in matches: #already sorted by match number
  print wikiCALrow(ms).encode('utf-8')
