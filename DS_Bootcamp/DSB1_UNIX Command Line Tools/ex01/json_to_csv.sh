#!/bin/bash
PATHJSON=../ex00/hh.json

jq -r -f filter.jq $PATHJSON > hh.csv

