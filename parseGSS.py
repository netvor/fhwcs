#!/usr/bin/python

from globals import TeamStat, getInFile, marshal
import string
from lxml import etree
from whohas import whohas

tree = etree.parse(getInFile('raw/standings.html'),etree.HTMLParser())
standings=list()

for letter in string.ascii_uppercase[:8]:
  table=tree.xpath('//table[@summary="Group Group %c"]'%(letter))[0]
  for row in table.findall('./tbody/tr'):
    [tdTeam,tdPlayed,tdWins,tdDraws,tdLosses,tdGoalsFor,tdGoalsAgainst,tdPoints]=row.getchildren()
    ts = TeamStat()
    ts.group = letter
    ts.teamCode = tdTeam.find('.//img').get('src')[-7:-4].upper()
    ts.teamName = tdTeam.find('.//img').get('title')
    ts.played = int(tdPlayed.text)
    ts.wins = int(tdWins.text)
    ts.draws = int(tdDraws.text)
    ts.losses = int(tdLosses.text)
    ts.goalsFor = int(tdGoalsFor.text)
    ts.goalsAgainst = int(tdGoalsAgainst.text)
    ts.goalsDiff = int(ts.goalsFor - ts.goalsAgainst)
    ts.points = int(tdPoints.text)
    
    standings.append(ts)

marshal(standings,'parsed/gss.pkl')
