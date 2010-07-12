#!/usr/bin/python

from globals import MatchStat, unmarshalMatches, counter
from operator import attrgetter
from optfunc import optfunc

def wikiMYCPGheader(prefix):
  if prefix: return '^  #  ^  No.  ^       When       ^  %-88s  ^    Yellow    ^     2Y=R     ^  Direct red  ^  Weighted Total  ^' % ('Match')
  else: return '^  No.  ^       When       ^  %-88s  ^    Yellow    ^     2Y=R     ^  Direct red  ^  Weighted Total  ^' % ('Match')

def wikiMYCPGrow(ms,prefix):
  _yellow = '%d (%d:%d)' % (ms.homeCards[0]+ms.awayCards[0], ms.homeCards[0], ms.awayCards[0])
  _yyr = '%d (%d:%d)' % (ms.homeCards[1]+ms.awayCards[1], ms.homeCards[1], ms.awayCards[1])
  _red = '%d (%d:%d)' % (ms.homeCards[2]+ms.awayCards[2], ms.homeCards[2], ms.awayCards[2])
  _total = '**%d** (%d:%d)' % (ms.homeCards[3]+ms.awayCards[3], ms.homeCards[3], ms.awayCards[3])
  if prefix: return '| %3d | %5d | %16s | %-90s | %-12s | %-12s | %-12s | %-16s |' % (counter.next(),ms.number, ms.when, ms.matchTitle(), _yellow, _yyr, _red, _total)
  else:return '| %5d | %16s | %-90s | %-12s | %-12s | %-12s | %-16s |' % (ms.number, ms.when, ms.matchTitle(), _yellow, _yyr, _red, _total)

def wikiMYCPG(num=10,prefix=False):
  matches=list()
  for ms in unmarshalMatches('parsed/match%02d.pkl'):
    if ms.hasResults:
      ms.totalCards = ms.homeCards[3]+ms.awayCards[3]
      matches.append(ms)

  print '\n\n==== Most yellow cards per game ====\n'.encode('utf-8')
  print wikiMYCPGheader(prefix).encode('utf-8')

  for ms in list(sorted( sorted(matches,key=lambda x:x.when_tm()) ,key=attrgetter('totalCards'), reverse=True))[:num]:
    print wikiMYCPGrow(ms,prefix).encode('utf-8')

optfunc.main(wikiMYCPG)
