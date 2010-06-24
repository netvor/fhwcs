#!/bin/bash

PDFS='raw/matchreports.pdfs.txt'

while read PDF
 do
  PDF="raw/matchreports/$PDF"
  TXT="${PDF%%.pdf}.txt"
#  [ -f "$TXT" ] && echo ">>> Skipping PDF file $PDF..." || (
  [ -f "$TXT" ] || (
    pdftotext -raw -enc 'UTF-8' "$PDF" "$TXT"
    echo "    >>> Decoding $PDF --> $TXT..."
    python parseMatchReport.py "$TXT"
    echo "    >>> Parsed $TXT."
  )
done < $PDFS
