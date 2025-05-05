#!/bin/bash
PATHCSV=../ex01/hh.csv

(head -n1 $PATHCSV && tail -n+2 $PATHCSV | sort -t "," -k 2,2 -k 1,1) > hh_sorted.csv

