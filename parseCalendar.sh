#!/bin/bash

CALENDARFILE='raw/calendar.html'
URLS='raw/calendar.urls'

grep -Eo '/worldcup/matches/[^/"]+/match=[0-9]+/[^/"]+.html' $CALENDARFILE |
  sort | uniq |
  tee $URLS | while read URL
   do
    OUTFILE=$(echo $URL | tr ':/' '__')
    [ -f "raw/matchpages/$OUTFILE" ] || ( wget -O "raw/matchpages/$OUTFILE" "http://www.fifa.com$URL" && python parseMatchPage.py "raw/matchpages/$OUTFILE" )
  done
