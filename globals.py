#!/usr/bin/python

from operator import attrgetter
import sys
import pickle

class TeamStat:
  pass
class MatchStat:
  pass

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
    print 'Cannot open input file <%s>!' % (inFileName)
    sys.exit(1)

def getOutFile(default,argi=2):
  try:
    outFileName = sys.argv[argi]
  except:
    outFileName = default
  try:
    outFile = open(outFileName,'w')
    return outFile
  except:
    print 'Cannot open output file <%s>!' % (outFileName)
    sys.exit(1)

def unmarshal(default,argi=1):
  return pickle.load(getInFile(default,argi))

def marshal(obj,default,argi=2):
  pickle.dump(obj,getOutFile(default,argi))

def unmarshalMatches(format,max=64):
  matches=list()
  for i in range(max):
    filename = format % (i)
    try:
      matches.append(pickle.load(open(filename,'r')))
    except:
      pass
  return matches
