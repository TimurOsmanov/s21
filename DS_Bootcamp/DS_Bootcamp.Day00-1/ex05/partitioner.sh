#!/bin/bash
PATHCSV=../ex03/hh_positions.csv

header=$(head -n1 ../ex03/hh_positions.csv)
str=$(head -n2 ../ex03/hh_positions.csv | tail -n1)

IFS='\"' read -a line <<< $str
date=${line[3]:0:10}

echo $header > $date.csv

while IFS='\"' read tab1 id tab2 created tab3 name test link 
do

  if [ "$date" = "${created:0:10}" ]; then
    echo "\"$id\",\"$created\",\"$name\"$test\"$link\"" >> $date.csv
  else 
    date=${created:0:10}
    echo $header > $date.csv
    echo "\"$id\",\"$created\",\"$name\"$test\"$link\"" >> $date.csv
  fi  
  
done <<< $(tail -n+2 $PATHCSV)

