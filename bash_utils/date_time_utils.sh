#!/bin/bash

#### Difference Calculation ########
FILE_MODIFIED_TIME=$(date -r /home/shadhini/dev/repos/shadhini/python_helpers/bash_utils/hello_world/original.txt +%s)
CURRENT=$(date +%s)

DIFF=$(((CURRENT-FILE_MODIFIED_TIME)/60))

echo $DIFF

