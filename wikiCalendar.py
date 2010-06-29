#!/usr/bin/python

from globals import MatchStat, unmarshalMatches
from optfunc import optfunc

def wikiCALheader():
  return '^  No.  ^       When       ^  %-88s  ^   Score   ^  Weighted Cards  ^        First Goal        ^' % ('Match')

def wikiCALrow(ms):
  if ms.hasResults:
    results = '%d:%d' % (len(ms.homeGoals),len(ms.awayGoals))
    try: firstgoal="**%d'** -- %s" % min(ms.goals())
    except: firstgoal='//(no goals)//'
    ycrc = '**%d** (%d:%d)' % (ms.homeCards[3]+ms.awayCards[3], ms.homeCards[3], ms.awayCards[3])
  else:
    results=''
    ycrc=''
    firstgoal=''
  return '| %5d | %16s | %-90s |  %7s  |  %-14s  | %-24s |' % (ms.number, ms.when, ms.matchTitle(), results, ycrc, firstgoal)

def wikiCAL(title='Calendar', start=1, end=64):
  matches = unmarshalMatches('parsed/match%02d.pkl', end, start)
  print ( '\n\n===== %s =====\n' % (title) ).encode('utf-8')
  print wikiCALheader().encode('utf-8')
  for ms in matches: #already sorted by match number
    print wikiCALrow(ms).encode('utf-8')

optfunc.main(wikiCAL)
