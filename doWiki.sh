#!/bin/bash

DWPAGE=/srv/www/beta.flyinghonzas.cz/htdocs/bin/dwpage.php

./fetchData.sh

python wikiGSS.py       > 'wiki/gss.txt'
python wikiLSIGS.py     > 'wiki/lsigs.txt'
python wikiCalendar.py  > 'wiki/calendar.txt'

cat 'wiki/header.txt'   > 'wiki/out.txt'
cat 'wiki/gss.txt'       >> 'wiki/out.txt'
cat 'wiki/lsigs.txt'     >> 'wiki/out.txt'
cat 'wiki/calendar.txt'  >> 'wiki/out.txt'
cat 'wiki/footer.txt'    >> 'wiki/out.txt'

$DWPAGE -m "Updated by doWiki.sh" commit 'wiki/out.txt' '2010 fifa world cup sweeps'
