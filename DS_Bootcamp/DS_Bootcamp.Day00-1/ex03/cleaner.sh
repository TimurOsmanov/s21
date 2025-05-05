#!/bin/bash
PATHCSV=../ex02/hh_sorted.csv

while IFS='\"' read tab1 id tab2 created tab3 name test link 
do
  if grep -q -i junior <<< $name; then
    echo "\"$id\",\"$created\",\"Junior\"$test\"$link\""
  elif grep -q -i middle <<< $name; then
    echo "\"$id\",\"$created\",\"Middle\"$test\"$link\""
  elif grep -q -i senior <<< $name; then
    echo "\"$id\",\"$created\",\"Senior\"$test\"$link\""
  else
    echo "\"$id\",\"$created\",\"-\"$test\"$link\""
  fi
done < $PATHCSV > name_cleared.csv

(cat $PATHCSV | head -n1; cat name_cleared.csv | tail -n+2) > hh_positions.csv

# clean dir
rm -rf name_cleared.csv

