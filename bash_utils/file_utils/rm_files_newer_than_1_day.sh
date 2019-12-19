NOW=$(date +%s)

cd /home/shadhini/dev/repos/shadhini/python_helpers/bash_utils/file_utils

for dir in $(ls -d */)
do
  #Do something, the directory is accessible with $d:
  echo $dir
  LAST_MODIFIED_DATE=$(date -r $dir +%s)
  DIFF=$(((NOW-LAST_MODIFIED_DATE)/60/60/24))
  echo $DIFF
  if [ $DIFF -lt 5 ]
  then
    echo "File is New!!!"
    rm -vr $dir
  fi
done >output_file