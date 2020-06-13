today=$(date -u -d '+5 hour +30 min' '+%F')
dirs=$(find /home/shadhini/dev/repos/shadhini/python_helpers/bash_utils/file_utils/res/ -name "$today"\*)
#dirs=(/mnt/disks/curwsl_nfs/mike/outputs/*/)
#echo $dirs
#for dir in "${dirs[@]}";
for dir in $dirs;
do
    echo "##########"
    echo "$dir"
done
