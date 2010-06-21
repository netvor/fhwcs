#!/usr/bin/python

from globals import MatchStat, getInFile, marshal, unmarshal
import re

### Part one: parsing the match report txt

fp = getInFile('')
fn = fp.name
contents = fp.read() # data is utf-8 encoded
contents = unicode(contents, 'utf-8')

codes = re.search(r'_(?P<h>[A-Z]{3})-(?P<a>[A-Z]{3})_',fn.upper()).groupdict()
assert(all(codes.values()))

matchTitleMatch = re.search(ur"(?<=^\u000c)(?P<aaaa>[^()]+) \((?P<a>[A-Z]{3})\)(?P<hhhh>[^()]+) \((?P<h>[A-Z]{3})\)$",contents,re.M)
assert(matchTitleMatch)
matchTitle = matchTitleMatch.group()
teams = matchTitleMatch.groupdict()
assert(all(teams.values()))
assert(all([ codes[key]==teams[key] for key in ['h','a'] ]))

scoreDict = re.search(r'^(?P<hhhh>.+) - (?P<aaaa>.+) (?P<hg>\d+):(?P<ag>\d)+( \(\d+:\d+\))?$',contents,re.M).groupdict()
assert(all([ scoreDict[key]==teams[key] for key in ['hhhh','aaaa'] ]))
score = ( int(scoreDict['hg']), int(scoreDict['ag']) )

goals=list()
goalsLine = re.match(r'Goals Scored:\n((?P<goals>.+)\n)?'+re.escape(matchTitle), contents, re.S).group('goals')
if goalsLine: 
  for m in re.finditer(r"\((?P<who>[A-Z]{3})\)\s(?P<when>\d+)'(\+(?P<whenplus>\d+))?(?P<og>\sown goal)?",goalsLine):
    d = m.groupdict()
    if d['og']: d['who'] = filter(lambda code : code!=d['who'], codes.values())[0]
    goals.append( ( int(d['when']), d['who'] ) )
else:
  assert(score==(0,0))
homeGoals = [ tup[0] for tup in filter(lambda tup : tup[1]==teams['h'], goals) ]
awayGoals = [ tup[0] for tup in filter(lambda tup : tup[1]==teams['a'], goals) ]

assert( (len(homeGoals),len(awayGoals)) == score )
assert( sum(score) == len(goals) )

cards = [ int(c) for c in re.search(r'\n(\d+)Cautions(\d+)\n(\d+)Expulsions due to Second Caution(\d+)\n(\d+)Direct Expulsions(\d+)\n',contents).groups() ]
homeCards = tuple( cards[1:6:2] + [ cards[1]+2*cards[3]+4*cards[5] ] )
awayCards = tuple( cards[0:5:2] + [ cards[0]+2*cards[2]+4*cards[4] ] )
assert(len(homeCards)==len(awayCards))

number = int( re.search(ur'(?<=2010# )\d+(?=\n\u000c)',contents).group() )
assert( number == int(re.search(u'(^|/)(?P<n>\d\d)_',fn).group('n')) )

report = { 'homeCode'  : teams['h']    , 
           'homeName'  : teams['hhhh'] ,
           'awayCode'  : teams['a']    ,
           'awayName'  : teams['aaaa'] ,
           'number'    : number        ,
           'goals'     : goals         ,
           'homeGoals' : homeGoals     ,
           'awayGoals' : awayGoals     ,
           'homeCards' : homeCards     ,
           'awayCards' : awayCards     }


### Part two: integrating the match report data with an existing MatchStat instance


ms=unmarshal('parsed/match%02d.pkl'%(report['number']),None)

assert(ms.homeCode == report['homeCode'])
assert(ms.awayCode == report['awayCode'])
assert(ms.homeName == report['homeName'])
assert(ms.awayName == report['awayName'])

ms.goalsCode  = report['goals']
ms.homeGoals  = report['homeGoals']
ms.awayGoals  = report['awayGoals']
ms.homeCards  = report['homeCards']
ms.awayCards  = report['awayCards']
ms.hasResults = True

res = '%d:%d' % (len(ms.homeGoals),len(ms.awayGoals))
try: fg="%d' -- %s" % min(ms.goalsCode)
except: fg='(no goals)'
print ( "Results of match %d:\n  %s:%s  %s\n  cards: %s : %s\n  first goal: %s" % ( 
  ms.number,
  ms.homeCode,
  ms.awayCode,
  res,
  '/'.join([str(c) for c in ms.homeCards]),
  '/'.join([str(c) for c in ms.awayCards]),
  fg ) ).encode('utf-8')

marshal(ms,'parsed/match%02d.pkl'%(ms.number),None)
