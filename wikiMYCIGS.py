#!/usr/bin/python

from globals import MatchStat, unmarshalMatches
from operator import itemgetter

cards=dict()
for ms in unmarshalMatches('parsed/match%02d.pkl',48):
  if ms.hasResults:
    for team in [ms.homeWiki, ms.awayWiki]: 
      if team not in cards: cards[team] = [0,0,0]
    cards[ms.homeWiki] = [old+new for old,new in zip(cards[ms.homeWiki],ms.homeCards)]
    cards[ms.awayWiki] = [old+new for old,new in zip(cards[ms.awayWiki],ms.awayCards)]

def wikiMYCIGSheader():
  return '^ %-50s ^  Yellow cards  ^  Direct red cards  ^  Total  ^' % ('Team')

def wikiMYCIGSrow(team, yellow,red,total):
  _total = '**%d**' % (total)
  return '| %-50s | %14d | %18d | %7s |' % (team,yellow,red,_total)

print '\n\n===== Most yellow cards in group stage =====\n'.encode('utf-8')
print wikiMYCIGSheader().encode('utf-8')

for (team,[yellow,red,total]) in list(reversed(sorted(cards.items(),key=lambda f:f[1][2])))[:10]:
  print wikiMYCIGSrow(team,yellow,red,total).encode('utf-8')
