#!/bin/bash

STANDINGSURL='http://www.fifa.com/worldcup/standings/index.html'
STANDINGSFILE='raw/standings.html'
CALENDARURL='http://www.fifa.com/worldcup/matches/calendar.html'
CALENDARFILE='raw/calendar.html'

#wget --progress=dot:binary -O $STANDINGSFILE $STANDINGSURL && python parseGSS.py
wget --progress=dot:binary -O $CALENDARFILE $CALENDARURL && ./parseCalendar.sh

./downloadMatchReports.sh && ./processMatchReports.sh
