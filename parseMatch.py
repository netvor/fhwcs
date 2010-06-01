#!/usr/bin/python

from globals import MatchStat, getInFile, marshal
from lxml import etree
from whohas import whohas

tree = etree.parse(getInFile(''),etree.HTMLParser())

div = tree.xpath('//div[@id="fwcMatchHeaderBgPre"]')[0]
ms = MatchStat()
ms.number = int(div.xpath('./div[@class="top"]/span[@class="L"]')[0].text[6:])
ms.group = div.xpath('./div[@class="top"]/span[@class="bold L"]/a')[0].text[6:].upper()
ms.when = div.xpath('./div[@class="top"]/span[@class="R"]')[0].text
ms.homeCode = div.xpath('./div[@class="middle"]/div[@class="hFlag flagImg "]/a/img')[0].get('src')[-7:-4].upper()
ms.homeName = div.xpath('./div[@class="middle"]/div[@class="teamh"]/a')[0].text
ms.homeWiki = u':%s: **%s** (%s)' % (ms.homeCode, whohas[ms.homeCode], ms.homeName)
ms.awayCode = div.xpath('./div[@class="middle"]/div[@class="aFlag flagImg"]/a/img')[0].get('src')[-7:-4].upper()
ms.awayName = div.xpath('./div[@class="middle"]/div[@class="teama"]/a')[0].text
ms.awayWiki = u':%s: **%s** (%s)' % (ms.awayCode, whohas[ms.awayCode], ms.awayName)
ms.hasResults = False

marshal(ms,'parsed/match%02d.pkl'%(ms.number))
