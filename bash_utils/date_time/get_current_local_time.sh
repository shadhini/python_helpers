#!/bin/bash

echo `date`
TODAY=$(date -u -d '+5 hour +30 min' '+%F +%T')
TODAY1=$(date -u -d '+5 hour +30 min' '+%F')

echo $TODAY
echo $TODAY1