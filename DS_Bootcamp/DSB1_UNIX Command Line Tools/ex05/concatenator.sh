#!/bin/bash
PATHCSV=../ex03/hh_positions.csv

(cat ../ex03/hh_positions.csv | head -n1; cat *csv | sort -u -t "," -k 2,2 -k 1,1 | head -n-1) > all.csv
diff all.csv ../ex03/hh_positions.csv

# that condidion $? is exit status of the last executed command
if [ $? -eq 0 ]; then
 echo the files are equal
else
 echo the files are different
fi

