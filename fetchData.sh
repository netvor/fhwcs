#!/bin/bash

STANDINGSURL='http://www.fifa.com/worldcup/standings/index.html'
STANDINGSFILE='raw/standings.html'
CALENDARURL='http://www.fifa.com/worldcup/matches/calendar.html'
CALENDARFILE='raw/calendar.html'

wget -O $STANDINGSFILE $STANDINGSURL && python parseGSS.py
# wget -O $CALENDARFILE $CALENDARURL && ./parseCalendar.sh
