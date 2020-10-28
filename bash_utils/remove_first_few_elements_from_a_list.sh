original="gs://wrf_nfs/mike/inputs/2020-06-10_16-00-00/mike_dis_2020-06-10_14-46-00.txt"
# first element in array
IFS='/' read -ra LIST <<< "$original"

filename="/mnt/disks"
for i in "${LIST[@]:2}"; do
    filename="$filename/$i"
done
echo $filename