#!/usr/bin/python

from globals import MatchStat, getInFile, marshal, unmarshal
from lxml import etree
from whohas import whohas
import sys, re

tree = etree.parse(getInFile(''),etree.HTMLParser())

div = tree.xpath('//div[@id="fwcMatchHeader"]')[0]
ms = MatchStat()
ms.number = int(div.xpath('./div[@class="footer"]/div[@class="info"]/span[@class="matchInfo L"]')[0].text[6:])

try:
  oldms = unmarshal('parsed/match%02d.pkl'%(ms.number),None)
  if isinstance(oldms,MatchStat):
    print "Skipping, parsed/match%02d.pkl exists"%(ms.number)
    sys.exit(0) # MatchStat exists, abort parsing.
except IOError:
  pass # file not found means go on, the MatchStat does not yet exist! 

assert(ms.number == int(div.xpath('./div[@class="footer"]/div[@class="info"]/span')[0].text[6:]))

ms.group = div.xpath('./div[@class="footer"]/div[@class="info"]/span')[1].text
ms.group = re.search('\w[\w\d ]+\w', ms.group).group()
if 'GROUP ' in ms.group.upper():
  ms.group = ms.group[6:].upper()


whdate = div.xpath('./div[@class="footer"]/div[@class="info"]/span')[2].text
whtime = div.xpath('./div[@class="match"]/div[@class="time"]')[0].text
ms.when = re.search('\d\d Ju[nl][ey]', whdate).group() + ' ' + re.search('\d?\d:\d\d', whtime).group()
ms.homeCode = div.xpath('./div[@class="match"]/div[@class="teamH"]/div[@class="flag"]/a/img')[0].get('src')[-7:-4].upper()
ms.homeName = div.xpath('./div[@class="match"]/div[@class="teamH"]/div[@class="name"]/a')[0].text
ms.awayCode = div.xpath('./div[@class="match"]/div[@class="teamA"]/div[@class="flag"]/a/img')[0].get('src')[-7:-4].upper()
ms.awayName = div.xpath('./div[@class="match"]/div[@class="teamA"]/div[@class="name"]/a')[0].text

assert( ms.homeCode.isalpha() )
assert( ms.awayCode.isalpha() )
assert( ms.homeName[0].isalpha() )
assert( ms.awayName[0].isalpha() )
assert( ms.homeName[-1].isalpha() )
assert( ms.awayName[-1].isalpha() )

ms.hasResults = False

marshal(ms,'parsed/match%02d.pkl'%(ms.number))
