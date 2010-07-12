#!/bin/bash

DWPAGE=/srv/www/beta.flyinghonzas.cz/htdocs/bin/dwpage.php

$DWPAGE -m "Updated by doWiki.sh" commit 'wiki/out.txt' '2010 fifa world cup sweeps'
$DWPAGE -m "Updated by doWiki.sh" commit 'wiki/out.gs.txt' '2010 fifa world cup sweeps/group stage'
$DWPAGE -m "Updated by doWiki.sh" commit 'wiki/out.fsr.txt' '2010 fifa world cup sweeps/final results'
