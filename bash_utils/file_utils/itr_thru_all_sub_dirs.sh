# iterate through all the sub directorires listed under a given directory


# including the parent directory
for dir in $(find /home/shadhini/dev/repos/shadhini/python_helpers/bash_utils/file_utils/ -maxdepth 1 -type d)
do
  #Do something, the directory is accessible with $d:
  echo $dir
  LAST_MODIFIED_DATE=$(date -r $dir +%s)
  echo $LAST_MODIFIED_DATE
done >output_file1

# without parent directory
cd /home/shadhini/dev/repos/shadhini/python_helpers/bash_utils/file_utils

for dir in $(ls -d */)
do
  #Do something, the directory is accessible with $d:
  echo $dir
done >output_file2