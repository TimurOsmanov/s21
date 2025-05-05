#!/bin/bash

curl -k -H 'User-Agent: api-test-agent' 'https://api.hh.ru/vacancies?text=data+scientist&per_page=20&page=0' | jq '.' > hh.json

