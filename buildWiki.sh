#!/bin/bash

python wikiGSS.py       > 'wiki/gss.txt'

python wikiMGS.py -p -n5  > 'wiki/mgs.txt'
cat 'wiki/hidden.start.txt' >> 'wiki/mgs.txt'
python wikiMGS.py -p -n999 | tail -n+5 >> 'wiki/mgs.txt'
cat 'wiki/hidden.end.txt' >> 'wiki/mgs.txt'

python wikiFG.py -p -n5  > 'wiki/fg.txt'
cat 'wiki/hidden.start.txt' >> 'wiki/fg.txt'
python wikiFG.py -p -n999 | tail -n+5  >> 'wiki/fg.txt'
cat 'wiki/hidden.end.txt' >> 'wiki/fg.txt'

python wikiMGPG.py -p -n5 > 'wiki/mgpg.txt'
cat 'wiki/hidden.start.txt' >> 'wiki/mgpg.txt'
python wikiMGPG.py -p -n999 | tail -n+5 >> 'wiki/mgpg.txt'
cat 'wiki/hidden.end.txt' >> 'wiki/mgpg.txt'

python wikiMYCPG.py -p -n5  > 'wiki/mycpg.txt'
cat 'wiki/hidden.start.txt' >> 'wiki/mycpg.txt'
python wikiMYCPG.py -p -n999 | tail -n+5  >> 'wiki/mycpg.txt'
cat 'wiki/hidden.end.txt' >> 'wiki/mycpg.txt'

python wikiMYCIGS.py -p -n5 > 'wiki/mycigs.txt'
cat 'wiki/hidden.start.txt' >> 'wiki/mycigs.txt'
python wikiMYCIGS.py -p -n999 | tail -n+5 >> 'wiki/mycigs.txt'
cat 'wiki/hidden.end.txt' >> 'wiki/mycigs.txt'

python wikiLSIGS.py -p -n5  > 'wiki/lsigs.txt'
cat 'wiki/hidden.start.txt' >> 'wiki/lsigs.txt'
python wikiLSIGS.py -p -n999 | tail -n+5  >> 'wiki/lsigs.txt'
cat 'wiki/hidden.end.txt' >> 'wiki/lsigs.txt'

python wikiCalendar.py -s49 > 'wiki/calendar.txt'
python wikiCalendar.py -e48 -t'Results' > 'wiki/calendar.gs.txt'
python wikiCalendar.py -t'Results' > 'wiki/calendar.fsr.txt'

cat 'wiki/header.txt'   > 'wiki/out.txt'
cat 'wiki/mgs.txt'       >> 'wiki/out.txt'
cat 'wiki/fg.txt'        >> 'wiki/out.txt'
cat 'wiki/mgpg.txt'      >> 'wiki/out.txt'
cat 'wiki/mycpg.txt'     >> 'wiki/out.txt'
cat 'wiki/mycigs.txt'    >> 'wiki/out.txt'
cat 'wiki/lsigs.txt'     >> 'wiki/out.txt'
#cat 'wiki/calendar.txt'  >> 'wiki/out.txt'
cat 'wiki/footer.txt'    >> 'wiki/out.txt'

cat 'wiki/header.gs.txt'   > 'wiki/out.gs.txt'
cat 'wiki/gss.txt'          >> 'wiki/out.gs.txt'
cat 'wiki/calendar.gs.txt'  >> 'wiki/out.gs.txt'
cat 'wiki/footer.gs.txt'    >> 'wiki/out.gs.txt'

cat 'wiki/header.fsr.txt'   > 'wiki/out.fsr.txt'
cat 'wiki/gss.txt'           >> 'wiki/out.fsr.txt'
cat 'wiki/calendar.fsr.txt'  >> 'wiki/out.fsr.txt'
cat 'wiki/footer.fsr.txt'    >> 'wiki/out.fsr.txt'
