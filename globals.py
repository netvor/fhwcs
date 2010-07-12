#!/usr/bin/python

from operator import attrgetter
import sys
import pickle
import time

counter=(i for i in xrange(1,1000))

class BaseStat:
  @staticmethod
  def wiki(code, name):
    from whohas import whohas
    return ':%s: **%s** (%s)' % (code, whohas[code], name)

class TeamStat(BaseStat):
  def teamWiki(self):
    return self.wiki(self.teamCode, self.teamName)

class MatchStat(BaseStat):
  def homeWiki(self):
    return self.wiki(self.homeCode, self.homeName)
  def awayWiki(self):
    return self.wiki(self.awayCode, self.awayName)
  def matchTitle(self):
    _group = self.group
    if len(_group)==1:
      _group = "Group " + _group
    return '%s: %s //vs.// %s' % (_group, self.homeWiki(), self.awayWiki())
  def goals(self):
    wiki = { self.homeCode : self.homeWiki(), self.awayCode : self.awayWiki() }
    return [ (minute,wiki[code]) for minute,code in self.goalsCode ]
  def when_tm(self):
    return time.strptime(self.when + ' 2010', '%d %B %H:%M %Y')

def teamSorted(teams):
  temp = sorted(teams, key=attrgetter('goalsFor'), reverse=True)
  temp = sorted(temp, key=attrgetter('goalsDiff'), reverse=True)
  temp = sorted(temp, key=attrgetter('points'), reverse=True)
  return temp

def getInFile(default,argi=1):
  try:
    inFileName = sys.argv[argi]
  except:
    inFileName = default
  try:
    inFile = open(inFileName,'r')
    return inFile
  except:
    raise IOError('Cannot open input file <%s>!' % (inFileName))

def getOutFile(default,argi=2):
  try:
    outFileName = sys.argv[argi]
  except:
    outFileName = default
  try:
    outFile = open(outFileName,'w')
    return outFile
  except:
    raise IOError('Cannot open output file <%s>!' % (outFileName))

def unmarshal(default,argi=1):
  return pickle.load(getInFile(default,argi))

def marshal(obj,default,argi=2):
  pickle.dump(obj,getOutFile(default,argi))

def unmarshalMatches(format,max=64,min=1):
  matches=list()
  for i in range(min,max+1):
    filename = format % (i)
    try:
      matches.append(pickle.load(open(filename,'r')))
    except:
      pass
  return matches
