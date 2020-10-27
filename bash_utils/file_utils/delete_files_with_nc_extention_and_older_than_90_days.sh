files=$(find /mnt/disks/wrf_nfs/ -name "*.nc" -type f -mtime +90)

for file in $files;
do
    echo "Deleting..."
    echo $file
    rm -v $file
    echo "Deleted"
done
