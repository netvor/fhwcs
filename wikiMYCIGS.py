#!/usr/bin/python

from globals import MatchStat, unmarshalMatches
from operator import itemgetter
from optfunc import optfunc

def wikiMYCIGSheader():
  return '^ %-50s ^  Yellow  ^  2Y=R  ^  Direct Red  ^  Weighted Total  ^' % ('Team')

def wikiMYCIGSrow(team, yellow, yyr, red, total):
  _total = '**%d**' % (total)
  return '| %-50s | %8d | %6d | %12s | %16s |' % (team,yellow,yyr,red,_total)

def wikiMYCIGS(num=10):
  cards=dict()
  for ms in unmarshalMatches('parsed/match%02d.pkl',48):
    if ms.hasResults:
      for team in [ms.homeWiki(), ms.awayWiki()]: 
        if team not in cards: cards[team] = (0,0,0,0)
      cards[ms.homeWiki()] = tuple( old+new for old,new in zip(cards[ms.homeWiki()],ms.homeCards) )
      cards[ms.awayWiki()] = tuple( old+new for old,new in zip(cards[ms.awayWiki()],ms.awayCards) )

  print '\n\n==== Most yellow cards in group stage ====\n'.encode('utf-8')
  print wikiMYCIGSheader().encode('utf-8')

  for (team,[yellow,yyr,red,total]) in list(reversed(sorted(cards.items(),key=lambda f:f[1][3])))[:num]:
    print wikiMYCIGSrow(team,yellow,yyr,red,total).encode('utf-8')

optfunc.main(wikiMYCIGS)
