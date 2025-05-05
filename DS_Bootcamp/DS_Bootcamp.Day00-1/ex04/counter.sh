#!/bin/bash
PATHCSV=../ex03/hh_positions.csv

junior=0
middle=0
senior=0

while IFS='\"' read tab1 id tab2 created tab3 name test link 
do
  if grep -q -i junior <<< $name; then
    ((junior+=1))
  elif grep -q -i middle <<< $name; then
    ((middle+=1))
  elif grep -q -i senior <<< $name; then
    ((senior+=1))
  fi
done < $PATHCSV 

echo '"name","count"' > hh_uniq_positions.csv
echo "\"Junior\"",$junior >> hh_uniq_positions.csv 
echo "\"Middle\"",$middle >> hh_uniq_positions.csv
echo "\"Senior\"",$senior >> hh_uniq_positions.csv

