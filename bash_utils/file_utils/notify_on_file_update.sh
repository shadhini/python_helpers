#!/bin/bash
# to be run every 5 mins

#### Difference Calculation ########
FILE_MODIFIED_TIME=$(date -r /home/shadhini/dev/repos/shadhini/python_helpers/bash_utils/hello_world/original.txt +%s)
CURRENT=$(date +%s)

DIFF=$(((CURRENT-FILE_MODIFIED_TIME)/60))
echo $DIFF

if [ $DIFF -lt 7 ]
then
  echo "File Updated!!!"
fi

