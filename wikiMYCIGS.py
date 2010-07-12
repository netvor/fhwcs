#!/usr/bin/python

from globals import MatchStat, unmarshalMatches, counter
from operator import itemgetter
from optfunc import optfunc

def wikiMYCIGSheader(prefix):
  if prefix: return '^  #  ^ %-50s ^  Yellow  ^  2Y=R  ^  Direct Red  ^  Weighted Total  ^' % ('Team')
  else: return '^ %-50s ^  Yellow  ^  2Y=R  ^  Direct Red  ^  Weighted Total  ^' % ('Team')

def wikiMYCIGSrow(team, yellow, yyr, red, total, prefix):
  _total = '**%d**' % (total)
  if prefix: return '| %3d | %-50s | %8d | %6d | %12s | %16s |' % (counter.next(),team,yellow,yyr,red,_total)
  else: return '| %-50s | %8d | %6d | %12s | %16s |' % (team,yellow,yyr,red,_total)

def wikiMYCIGS(num=10,prefix=False):
  cards=dict()
  for ms in unmarshalMatches('parsed/match%02d.pkl',48):
    if ms.hasResults:
      for team in [ms.homeWiki(), ms.awayWiki()]: 
        if team not in cards: cards[team] = (0,0,0,0)
      cards[ms.homeWiki()] = tuple( old+new for old,new in zip(cards[ms.homeWiki()],ms.homeCards) )
      cards[ms.awayWiki()] = tuple( old+new for old,new in zip(cards[ms.awayWiki()],ms.awayCards) )

  print '\n\n==== Most yellow cards in group stage ====\n'.encode('utf-8')
  print wikiMYCIGSheader(prefix).encode('utf-8')

  for (team,[yellow,yyr,red,total]) in list(reversed(sorted(cards.items(),key=lambda f:f[1][3])))[:num]:
    print wikiMYCIGSrow(team,yellow,yyr,red,total,prefix).encode('utf-8')

optfunc.main(wikiMYCIGS)
