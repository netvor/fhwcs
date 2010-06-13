#!/bin/bash

./fetchData.sh

python wikiGSS.py       > 'wiki/gss.txt'
python wikiMGS.py       > 'wiki/mgs.txt'
python wikiFG.py        > 'wiki/fg.txt'
python wikiMGPG.py      > 'wiki/mgpg.txt'
python wikiMYCPG.py     > 'wiki/mycpg.txt'
python wikiMYCIGS.py    > 'wiki/mycigs.txt'
python wikiLSIGS.py     > 'wiki/lsigs.txt'
python wikiCalendar.py  > 'wiki/calendar.txt'

cat 'wiki/header.txt'   > 'wiki/out.txt'
cat 'wiki/gss.txt'       >> 'wiki/out.txt'
cat 'wiki/mgs.txt'       >> 'wiki/out.txt'
cat 'wiki/fg.txt'        >> 'wiki/out.txt'
cat 'wiki/mgpg.txt'      >> 'wiki/out.txt'
cat 'wiki/mycpg.txt'     >> 'wiki/out.txt'
cat 'wiki/mycigs.txt'    >> 'wiki/out.txt'
cat 'wiki/lsigs.txt'     >> 'wiki/out.txt'
cat 'wiki/calendar.txt'  >> 'wiki/out.txt'
cat 'wiki/footer.txt'    >> 'wiki/out.txt'
