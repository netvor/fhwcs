#!/bin/bash

#STARTURL='http://www.fifa.com/worldcup/organisation/documents/matchdocumentgroup.html'
STARTURL='http://www.fifa.com/worldcup/organisation/documents/matchdocumentkophase.html'
STARTFILE='raw/matchreports.html'
URLS='raw/matchreports.urls.txt'
PDFS='raw/matchreports.pdfs.txt'

wget --progress=dot:binary -O "$STARTFILE" "$STARTURL" || echo ">>> Error downloading $STARTURL!"
rm $PDFS
grep -Eo '<a[^>]+>\s*Match Report\s*</a>' "$STARTFILE" | grep -o 'href="[^"]*' | cut -c7- | sed 's/%5f/_/g' |
  tee $URLS | while read URL
   do
    BN=$(basename "$URL")
    OF=$(echo "$BN" | tr ':/' '__')
    URL="http://www.fifa.com$URL"
#    [ -f "raw/matchreports/$OF" ] && echo ">>> Skipping $OF..." || ( wget --progress=dot:binary -O "raw/matchreports/$OF" "$URL" && echo ">>> Downloaded $OF." )
    ! [ -f "raw/matchreports/$OF" ] && wget --progress=dot:binary -O "raw/matchreports/$OF" "$URL" && echo ">>> Downloaded $OF."
    echo $OF >> $PDFS
  done

