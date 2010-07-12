#!/usr/bin/python

from globals import MatchStat, unmarshalMatches, counter
from operator import itemgetter
from optfunc import optfunc

def wikiFGheader(prefix):
  if prefix: return '^  #  ^ %-50s ^  Minute  ^' % ('Team')
  else: return '^ %-50s ^  Minute  ^' % ('Team')

def wikiFGrow(team, minute,prefix):
  if prefix:
    return "| %3d | %-50s | %7d' |" % (counter.next(),team,minute)
  else:
    return "| %-50s | %7d' |" % (team,minute)

def wikiFG(num=10,prefix=False):
  goals=list()
  for ms in unmarshalMatches('parsed/match%02d.pkl'):
    if ms.hasResults:
      goals += ms.goals()

  print '\n\n==== Fastest goal ====\n'.encode('utf-8')
  print wikiFGheader(prefix).encode('utf-8')

  for (minute,team) in sorted(goals, key=itemgetter(0))[:num]:
    print wikiFGrow(team,minute,prefix).encode('utf-8')

optfunc.main(wikiFG)
