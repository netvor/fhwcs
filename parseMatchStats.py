#!/usr/bin/python

from globals import MatchStat, getInFile, marshal
from lxml import etree
from whohas import whohas
import re

tree = etree.parse(getInFile(''),etree.HTMLParser())

div = tree.xpath('//div[@id="fwcMatchHeader"]')[0]
parsedNumber = int(div.xpath('./div[@class="footer"]/div[@class="info"]/span[@class="matchInfo L"]')[0].text[6:])
filename='parsed/match%02d.pkl'%(parsedNumber)
assert(ms.number==parsedNumber)

assert( ms.group == div.xpath('./div[@class="footer"]/div[@class="info"]/span[@class="L"]/a')[0].text[6:].upper() )
assert( ms.homeCode == div.xpath('./div[@class="match"]/div[@class="teamH"]/div[@class="flag"]/a/img')[0].get('src')[-7:-4].upper() )
assert( ms.awayCode == div.xpath('./div[@class="match"]/div[@class="teamA"]/div[@class="flag"]/a/img')[0].get('src')[-7:-4].upper() )

_result=div.xpath('./div[@class="resultWrapper"]/div[@class="result"]')[0].text
result=re.findall('(\d+):(\d+)', _result)[0]
for hS in div.xpath('./div[@class="scorer"]//div[@class="home"]/ul/li'):
  


ms.hasResults = False

#marshal(ms,'parsed/match%02d.pkl'%(ms.number))
