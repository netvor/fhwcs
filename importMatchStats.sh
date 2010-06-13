#!/bin/bash

URL="$1"
OUTFILE=$(echo $URL | tr ':/' '__')

wget -O "raw/$OUTFILE" "$URL" && python parseMatchStats.py "raw/$OUTFILE"
